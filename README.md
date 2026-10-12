# GemiScrape

<p align="center">
  <img src="assets/logo.jpeg" alt="GemiScrape logo" width="220">
</p>

<p align="center">
  AI-powered web scraping directly from your terminal.
  <br>
  Extract, parse, and structure web data with Google Gemini.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-64748b?style=flat-square" alt="Supported platforms">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/AI-Google%20Gemini-8E75B2?style=flat-square" alt="Google Gemini">
</p>

---

GemiScrape is a command-line tool designed to extract and structure web content using Google Gemini.

Built for developers, researchers, and curious users who want to turn web pages into useful, structured data without a complicated setup.

## Features

* **AI-powered parsing** — Analyze web content and extract relevant information.
* **API-less approach** — Designed to work without a conventional API key, depending on the supported access method.
* **Cross-platform** — Intended for Windows, Linux, and macOS.
* **Flexible configuration** — Customize supported settings through `config.json`.
* **Multiple export formats** — Save results as JSON, Markdown, or plain text.
* **Terminal-first workflow** — Access extraction features directly from the command line.

## Requirements

* Python 3
* Git
* pip
* Internet connection
* A supported method of accessing Google Gemini

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Idol2me/GemiScrape.git
cd GemiScrape
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

On systems where Python is invoked as `python3`, use:

```bash
python3 -m pip install -r requirements.txt
```

### Windows

```powershell
py -m pip install -r requirements.txt
```

### Linux and macOS

```bash
python3 -m pip install -r requirements.txt
```

## Usage

Check the available commands using the project's entry point:

```bash
python main.py --help
```

Replace `main.py` if your entry-point filename is different.

## Configuration

GemiScrape uses `config.json` for supported settings, which may include:

* Gemini model selection
* Cookies
* Request timeouts
* Terminal themes

Check the configuration file for the exact available options.

## Export Formats

| Format   | Description                                  |
| -------- | -------------------------------------------- |
| JSON     | Structured data for applications and scripts |
| Markdown | Readable, formatted content                  |
| TXT      | Plain-text output                            |

## Security

GemiScrape is designed as a web data extraction tool, not an autonomous AI agent.

* Treat scraped content as untrusted input.
* Never expose session cookies or credentials.
* Respect website terms and access restrictions.
* Review dependencies before running the project.

Its actual file access and execution capabilities depend on the implementation and configured permissions.

## Contributing

Contributions, bug reports, and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make and test your changes.
4. Submit a pull request.

## License

Check the repository for license information before redistributing or modifying this project.

---

<p align="center">
  <sub>GemiScrape — Extract. Structure. Simplify.</sub>
</p>
