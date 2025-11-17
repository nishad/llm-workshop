---
title: Prerequisites
weight: 1
---

## System Requirements

To participate fully in this workshop, your system should meet the following requirements:

### Minimum Requirements

| Component | Requirement |
|-----------|-------------|
| **RAM** | 8 GB (16 GB recommended) |
| **Storage** | 20 GB free space (for Ollama, models, and tools) |
| **OS** | Windows 11, macOS 12 Sonoma or later, or Linux |
| **Internet** | Stable broadband connection (for downloading 2-5 GB of models) |
| **Processor** | Modern CPU (Intel/AMD/Apple Silicon) |

### Recommended Specifications

For optimal performance:
- **RAM**: 16 GB or more
- **Storage**: 50 GB free (SSD preferred for faster model loading)
- **GPU**: Not required, but Apple Silicon (M1/M2/M3) or NVIDIA GPU will improve performance

{{< callout type="info" >}}
**Good News**: Modern laptops from the past 5 years typically meet these requirements. You don't need expensive hardware to run local LLMs!
{{< /callout >}}

## Pre-Workshop Setup

### Part 1: For Everyone

You can complete these steps **before** the workshop to save time during the live session:

#### 1. Install Ollama

**Download and install Ollama** from the official website:

{{< cards >}}
  {{< card link="https://ollama.com/download" title="Download Ollama" icon="download" >}}
{{< /cards >}}

- **macOS**: Download the `.dmg` file and drag to Applications
- **Windows**: Download the `.exe` installer and run it
- **Linux**: Follow the installation script on the download page

#### 2. Verify Installation

After installing, launch the Ollama application:

- On **macOS/Windows**: Look for the Ollama icon in your Applications folder or Start menu
- On **Linux**: Run `ollama` in the terminal

You should see the Ollama GUI interface open.

{{< callout type="warning" >}}
**First-time users**: Ollama may ask for permissions to run on your system. Please allow these permissions for the workshop.
{{< /callout >}}

#### 3. Download Llama 3.2 Model (Optional)

To save time during the workshop, you can pre-download the Llama 3.2 model:

**Option 1: Using the GUI** (Recommended)
1. Open Ollama
2. Click on the model dropdown
3. Search for "llama3.2"
4. Click download (approximately 2 GB)

**Option 2: Using the Terminal**
```bash
ollama pull llama3.2
```

This downloads the 3B parameter version, which is perfect for the workshop.

### Part 2: For Python Integration (Optional)

If you plan to actively follow along with **Part 2** of the workshop (Python, embeddings, and RAG), please set up your Python environment:

#### 1. Install Python

Ensure you have **Python 3.8 or later** installed:

```bash
python --version
# or
python3 --version
```

If you need to install Python:
- **macOS/Linux**: Use your package manager or download from [python.org](https://www.python.org/downloads/)
- **Windows**: Download from [python.org](https://www.python.org/downloads/) (ensure "Add Python to PATH" is checked)

#### 2. Install Jupyter Notebook

```bash
pip install jupyter notebook
# or
pip3 install jupyter notebook
```

#### 3. Install Required Libraries

```bash
pip install ollama chromadb jinja2
```

{{< callout type="info" >}}
**Don't worry if you skip this section**: You can still follow along with Part 2 conceptually. The Python setup is optional for hands-on coding during the workshop.
{{< /callout >}}

## What to Have Ready

On the day of the workshop, please have:

- [ ] **Ollama installed** and tested
- [ ] **Llama 3.2 model downloaded** (optional but recommended)
- [ ] **Text editor or IDE** of your choice (VS Code, PyCharm, Sublime, etc.)
- [ ] **Terminal/Command Prompt** access
- [ ] **Jupyter Notebook** (for Part 2)
- [ ] **Workshop notebooks cloned** from the repository (see below)

## Cloning the Workshop Notebooks

Before or during the workshop, clone the companion notebook repository:

```bash
git clone https://github.com/nishad/llm-workshop-notebooks.git
cd llm-workshop-notebooks
```

If you don't have `git` installed, you can download the repository as a ZIP file from GitHub.

## Troubleshooting Before the Workshop

### Ollama Won't Start

- **macOS**: Check System Preferences → Privacy & Security → Allow Ollama
- **Windows**: Right-click Ollama → Run as Administrator
- **Linux**: Ensure you have the necessary permissions and dependencies

### Model Download Fails

- Check your internet connection
- Ensure you have enough disk space (at least 5 GB free)
- Try downloading via terminal: `ollama pull llama3.2`
- If slow, the download will resume if interrupted

### Python Issues

- Use a virtual environment: `python -m venv workshop-env`
- Activate it: `source workshop-env/bin/activate` (Mac/Linux) or `workshop-env\Scripts\activate` (Windows)
- Install packages in the virtual environment

## Getting Help

If you encounter issues before the workshop:

1. Check the [FAQ](/v2/faq) page
2. Review the [Troubleshooting](/v2/part1-fundamentals/03-setup/troubleshooting) guide
3. Join the workshop with your questions - we'll address setup issues at the start

{{< callout type="success" >}}
**Ready to Go?** If you've completed the pre-workshop setup, you're all set! See you at the workshop!
{{< /callout >}}

## Next Steps

{{< cards >}}
  {{< card link="/v2/part1-fundamentals" title="Part 1: Fundamentals" icon="arrow-right" subtitle="Begin with LLM concepts and setup" >}}
{{< /cards >}}
