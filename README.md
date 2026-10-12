# GemiScrape 🚀

<p align="center">
  <img src="https://i.postimg.cc/Gpn5vxGD/Gemini-Generated-Image-2babaj2babaj2bab.jpg" alt="GemiScrape Logo" width="220">
</p>

<p align="center">
  <strong>AI-powered web scraping from your terminal.</strong>
  <br>
  Extract, parse, and structure web data with Google Gemini.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/AI-Google%20Gemini-8E75B2?style=flat-square" alt="Google Gemini">
  <img src="https://img.shields.io/badge/Platform-Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux">
</p>

---

GemiScrape is a lightweight command-line interface (CLI) tool designed to extract and structure web content using Google Gemini.

Built for developers who want to turn unstructured web data into useful output directly from the terminal, without a traditional API setup.

> [!IMPORTANT]
> **Security & Scope**
>
> GemiScrape is a data extraction tool, not an autonomous AI agent. It is not designed to execute arbitrary system commands. File access and modifications depend on the implemented export features and the permissions granted to the program.

## ✨ Features

* 🤖 **AI-Powered Parsing** — Use Google Gemini to analyze web content and extract relevant information.
* 🔑 **API-less Approach** — Designed to work without a conventional API key, depending on the supported access method.
* ⚡ **Lightweight CLI** — Run extraction workflows directly from your terminal.
* ⚙️ **Flexible Configuration** — Customize supported models, cookies, timeouts, and themes through `config.json`.
* 📊 **Multiple Export Formats** — Export extracted data as JSON, Markdown, or plain text.
* 🐧 **Linux-Friendly** — Designed with terminal-based workflows in mind.

## 📋 Requirements

* Python 3
* Git
* pip
* Internet connection
* A supported method of accessing Google Gemini

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Idol2me/GemiScrape.git
cd GemiScrape
```

### 2. Install dependencies

```bash
python3 -m pip install -r requirements.txt
```

### Optional: Use a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## ⚙️ Configuration

GemiScrape supports configuration through `config.json`.

Depending on your version, available settings may include:

* **Model:** Configure the supported Gemini model.
* **Cookies:** Set cookies when required by the access method.
* **Timeouts:** Adjust request time limits.
* **Theme:** Customize the CLI appearance.

Check the configuration file for the exact supported options and default values.

## 🚀 Usage

To check the available commands, run the project's CLI entry point:

```bash
python3 main.py --help
```

Replace `main.py` with the actual entry-point filename if necessary.

## 📦 Export Formats

| Format   | Purpose                                      |
| -------- | -------------------------------------------- |
| JSON     | Structured data for scripts and applications |
| Markdown | Readable output for documentation            |
| TXT      | Plain-text output for simple processing      |

## 🔒 Security & Responsible Use

* Respect website terms of service and access restrictions.
* Never share authentication cookies or session credentials.
* Treat scraped content as untrusted input.
* Review dependencies before running the project.
* Use export features only with intended file paths.

**Note:** API-less does not mean offline. The tool may still rely on network access, browser sessions, cookies, or third-party services.

## 🗺️ Roadmap

* [ ] Improve extraction accuracy.
* [ ] Expand CLI options.
* [ ] Add custom extraction templates.
* [ ] Improve error handling and diagnostics.
* [ ] Expand documentation with practical examples.

## 🤝 Contributing

Contributions, suggestions, and bug reports are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Test your changes.
5. Submit a pull request.

## 📜 License

Check the repository for license information before redistributing or modifying this project.

---

<p align="center">
  <strong>GemiScrape</strong>
  <br>
  <sub>Extract. Structure. Simplify.</sub>
</p>
