
#!/usr/bin/env python3
# GemiScrape - A small Gemini Web CLI.
# Built with a little patience, browser automation, and too much coffee.

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from playwright.sync_api import (
    sync_playwright,
    TimeoutError as PlaywrightTimeoutError,
)
from rich.console import Console
from rich.live import Live
from rich.panel import Panel
from rich.text import Text


APP_NAME = "GemiScrape"
VERSION = "1.1.0"

GEMINI_URL = "https://gemini.google.com/app"
PROFILE_DIR = Path.home() / ".gemiscrape" / "browser"

console = Console()
err_console = Console(stderr=True)


# The original project mark. Keeping the rough edges is part of the charm.
ASCII_ART = r"""
                                                 ==
                                                 ==
                                                 ==
                                                 ==
                                                ====
                                                ====
                                                ====
                                               ======
                                              +=======
                                              +++=====
                                             +++++=====
                                            +++++++=====
                                           *+++++++++====
                                          **++++++++++====
                                         *****+++++++++=====
                                       ********++++++++++====
                                      +**********+++++++++====
                                    *++***********++++++++++====
                                   *++++***********++++++++++====
                                ++*++++++************+++++++++======
                               *++++++++++++***********++++++++++======
                             ++++++++++++++++***********++++++++++=======
                          ++++++++++++++++++++************+++++++++=========
                      *+*++++++++++++++++++++++++**********++++++++++===========
                  *+**+++++++++++++++++++++++++++***********++++++++++==============
             +*+++++++++++++++++++++++++++++++++++++**********+++++++++==================
  ++++++++++++++++++++++++++++++++++++++++++++++++++*+*********++++++++++===========================
             ++**++++++++++++++++++++++++++++++++++++***********++++++++++===============
                  *+++++++++++++++++++++++++++++++++++++**********+++++++++=========
                      ++++++++++++++++++++++++++++++++++***********++++++++++===
                          ++++++++++++++++++++++++++++++++***********+++++++
                             ++++++++++++++++++++++++++++++***********+++
                               ++++++++++++++++++++++++++++++**********
                                 +++++++++++++++++++++++++++++*******
                                   *++++++++++++++++++++++++++++***
                                     *++++++++++++++++++++++++++*
                                       ++++++++++++++++++++++++
                                        *+++++++++++++++++++**
                                         +*++++++++++++++++**
                                           ++++++++++++++++
                                            *++++++++++++*
                                             *++++++++++*
                                              ++++++++++
                                               ++++++++
                                               +++++++*
                                                *+++++
                                                 ++++
                                                 *+++
                                                 ++**
                                                  ++
                                                  **
                                                  ++
                                                  +*
"""


def show_banner() -> None:
    """A terminal should have a little personality."""
    console.print(
        Text(ASCII_ART, style="bright_blue"),
        highlight=False,
    )
    console.print(
        Panel(
            f"[bold bright_blue]{APP_NAME}[/bold bright_blue] "
            f"[dim]v{VERSION}[/dim]\n"
            "[white]Gemini Web CLI — no conventional API key[/white]",
            border_style="blue",
        )
    )


def find_prompt_box(page):
    # Gemini changes its frontend sometimes, so keep a few fallbacks.
    selectors = [
        "rich-textarea [contenteditable='true']",
        "[role='textbox'][contenteditable='true']",
        "textarea",
    ]

    for selector in selectors:
        locator = page.locator(selector).first
        try:
            locator.wait_for(state="visible", timeout=2000)
            return locator
        except PlaywrightTimeoutError:
            continue

    raise RuntimeError(
        "Campo de mensagem não encontrado. "
        "A interface do Gemini pode ter mudado."
    )


def find_send_button(page):
    selectors = [
        "button[aria-label='Send message']",
        "button[aria-label='Enviar mensagem']",
        "button[aria-label*='Send']",
        "button[aria-label*='Enviar']",
    ]

    for selector in selectors:
        button = page.locator(selector).first

        try:
            if button.is_visible() and button.is_enabled():
                return button
        except Exception:
            continue

    return None


def latest_response_locator(page):
    # Read the actual response container instead of a nested sentence.
    for selector in [
        "model-response",
        ".model-response-text",
    ]:
        locator = page.locator(selector)

        try:
            if locator.count() > 0:
                return locator.last
        except Exception:
            continue

    return None


def read_latest_response(page) -> str:
    locator = latest_response_locator(page)

    if locator is None:
        return ""

    try:
        return locator.inner_text().strip()
    except Exception:
        return ""


def is_generation_active(page) -> bool:
    """Check common stop-generation controls in the Gemini interface."""
    try:
        return page.evaluate("""() => {
            const labels = Array.from(
                document.querySelectorAll('button')
            ).map(button => [
                button.getAttribute('aria-label') || '',
                button.getAttribute('title') || '',
                button.innerText || ''
            ].join(' ').toLowerCase());

            return labels.some(label =>
                /stop generating|stop response|stop generation|parar geração|parar resposta|interromper resposta/.test(label)
            );
        }""")
    except Exception:
        return False


def wait_for_new_response(page, previous_count: int) -> None:
    """Wait for Gemini to create a response container."""
    page.wait_for_function(
        """previous => {
            const responses = document.querySelectorAll('model-response');
            return responses.length > previous;
        }""",
        arg=previous_count,
        timeout=60000,
    )


def stream_response(page, previous_count: int) -> str:
    """
    Follow the newest response while Gemini is generating it.

    If the UI doesn't expose a reliable generation indicator, fall
    back to detecting when the response text stops changing.
    """
    wait_for_new_response(page, previous_count)

    console.print(
        "\n[bold bright_blue]Gemini[/bold bright_blue] "
        "[dim]está escrevendo...[/dim]\n"
    )

    answer = ""
    last_change = time.monotonic()
    started = time.monotonic()
    max_wait = 240
    stable_for = 3.0

    # Live updates let Rich redraw the answer as new text arrives.
    with Live(
        Text(""),
        console=console,
        refresh_per_second=10,
        vertical_overflow="visible",
    ) as live:
        while time.monotonic() - started < max_wait:
            current = read_latest_response(page)

            if current and current != answer:
                answer = current
                last_change = time.monotonic()
                live.update(Text(answer, style="white"))

            active = is_generation_active(page)
            stable_time = time.monotonic() - last_change

            # Best case: the UI tells us generation has stopped.
            if answer and not active and stable_time >= stable_for:
                break

            # Fallback: some UI versions don't expose a stop button.
            if answer and stable_time >= stable_for:
                break

            time.sleep(0.2)

    # One last read, just in case the final DOM update arrived late.
    final_answer = read_latest_response(page)
    if final_answer:
        answer = final_answer

    if not answer:
        raise RuntimeError(
            "Nenhuma resposta foi encontrada. "
            "Confira se o Gemini terminou de carregar."
        )

    return answer


def ask_gemini(page, prompt: str) -> str:
    # Count old responses so we don't accidentally print the previous one.
    previous_count = page.locator("model-response").count()

    editor = find_prompt_box(page)
    editor.fill(prompt)

    send_button = find_send_button(page)

    if send_button:
        send_button.click()
    else:
        # Enter is the fallback used by many versions of the UI.
        editor.press("Enter")

    return stream_response(page, previous_count)


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="gemiscrape",
        description="Chat with Gemini through its web interface.",
    )

    parser.add_argument(
        "prompt",
        nargs="?",
        help="Prompt to send immediately",
    )
    parser.add_argument(
        "--headed",
        action="store_true",
        help="Show the browser window for debugging or login",
    )

    args = parser.parse_args()
    PROFILE_DIR.mkdir(parents=True, exist_ok=True)

    show_banner()

    try:
        with sync_playwright() as playwright:
            context = playwright.chromium.launch_persistent_context(
                user_data_dir=str(PROFILE_DIR),
                headless=not args.headed,
                viewport={"width": 1280, "height": 900},
            )

            try:
                page = (
                    context.pages[0]
                    if context.pages
                    else context.new_page()
                )

                console.print("[dim]Conectando ao Gemini...[/dim]")
                page.goto(
                    GEMINI_URL,
                    wait_until="domcontentloaded",
                    timeout=60000,
                )

                console.print(
                    "[green]Página carregada.[/green] "
                    "Se necessário, faça login com --headed."
                )

                while True:
                    prompt = args.prompt

                    if prompt is None:
                        try:
                            prompt = console.input(
                                "\n[bold cyan]Você > [/bold cyan]"
                            )
                        except (EOFError, KeyboardInterrupt):
                            break

                    if prompt.strip().lower() in {
                        "exit", "quit", "sair"
                    }:
                        console.print("[dim]Até mais![/dim]")
                        break

                    if not prompt.strip():
                        if args.prompt is not None:
                            break
                        continue

                    try:
                        answer = ask_gemini(page, prompt)
                        console.print()
                        console.print(
                            Panel(
                                answer,
                                title="[bold bright_blue]Resposta final[/bold bright_blue]",
                                border_style="blue",
                                padding=(1, 2),
                            )
                        )
                    except PlaywrightTimeoutError:
                        console.print(
                            "[yellow]O Gemini demorou demais. "
                            "Tente novamente ou use --headed para depurar.[/yellow]"
                        )
                    except Exception as exc:
                        console.print(f"[red]Erro:[/red] {exc}")

                    if args.prompt is not None:
                        break

            finally:
                context.close()

    except KeyboardInterrupt:
        console.print("\n[dim]Encerrado pelo usuário.[/dim]")
        return 130
    except Exception as exc:
        err_console.print(f"[red]Falha ao iniciar:[/red] {exc}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())