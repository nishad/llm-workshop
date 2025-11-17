---
title: Python Setup
weight: 1
---

## Setting Up Python Environment for Ollama

This page guides you through setting up Python and the necessary libraries for working with Ollama programmatically.

---

## Step 1: Verify Python Installation

First, check if Python is installed and which version you have:

```bash
python --version
# or
python3 --version
```

**Required**: Python 3.8 or later

{{< callout type="info" >}}
**macOS/Linux Note**: You might need to use `python3` instead of `python` depending on your system configuration.
{{< /callout >}}

### Install Python (if needed)

If Python isn't installed or the version is too old:

**macOS**:
```bash
# Using Homebrew
brew install python@3.11
```

**Windows**:
- Download from [python.org](https://www.python.org/downloads/)
- **Important**: Check "Add Python to PATH" during installation

**Linux** (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip
```

---

## Step 2: Create a Virtual Environment (Recommended)

Virtual environments keep project dependencies isolated:

```bash
# Create a virtual environment
python3 -m venv workshop-env

# Activate it
# macOS/Linux:
source workshop-env/bin/activate

# Windows:
workshop-env\Scripts\activate
```

You'll see `(workshop-env)` in your terminal prompt when activated.

{{< callout type="warning" >}}
**Always activate** your virtual environment before installing packages or running scripts for this workshop.
{{< /callout >}}

---

## Step 3: Install Required Libraries

With your virtual environment activated, install the necessary packages:

```bash
pip install ollama chromadb jinja2 jupyter
```

**Library Purposes**:
- `ollama`: Official Ollama Python client
- `chromadb`: Vector database for embeddings
- `jinja2`: Template engine for dynamic prompts
- `jupyter`: Interactive notebooks for experimentation

### Verify Installation

```bash
pip list | grep -E 'ollama|chromadb|jinja2|jupyter'
```

Expected output (versions may vary):
```
chromadb        0.4.22
jinja2          3.1.2
jupyter         1.0.0
ollama          0.6.1
```

---

## Step 4: Test Ollama Connection

Create a test script to verify everything works:

**test_ollama.py**:
```python
import ollama

def test_connection():
    """Test connection to Ollama server."""
    try:
        # List available models
        models = ollama.list()
        print("✓ Connected to Ollama successfully!")
        print(f"\nAvailable models:")
        for model in models['models']:
            print(f"  - {model['name']}")
        return True
    except Exception as e:
        print(f"✗ Connection failed: {e}")
        print("\nTroubleshooting:")
        print("1. Make sure Ollama is running")
        print("2. Check if you can access http://localhost:11434")
        print("3. Try restarting Ollama")
        return False

if __name__ == "__main__":
    test_connection()
```

Run the test:
```bash
python test_ollama.py
```

**Expected Output**:
```
✓ Connected to Ollama successfully!

Available models:
  - llama3.2:latest
```

{{< callout type="error" >}}
**Connection Failed?**

If you see an error:
1. Make sure Ollama application is running
2. Verify port 11434 is accessible: `curl http://localhost:11434/api/tags`
3. Check firewall settings
4. Restart Ollama application

See [Troubleshooting](/v2/part1-fundamentals/03-setup/troubleshooting#connection-issues) for more help.
{{< /callout >}}

---

## Step 5: Install Jupyter Notebook

If you want to follow along with the workshop notebooks:

```bash
# Install Jupyter (already done above)
pip install jupyter

# Start Jupyter
jupyter notebook
```

This opens a browser window with Jupyter interface.

### Alternative: JupyterLab

For a more modern interface:

```bash
pip install jupyterlab
jupyter lab
```

---

## Step 6: Clone Workshop Notebooks

Get the companion notebooks for hands-on practice:

```bash
# Clone the repository
git clone https://github.com/nishad/llm-workshop-notebooks.git

# Navigate to it
cd llm-workshop-notebooks

# Install requirements (if not already done)
pip install -r requirements.txt

# Start Jupyter
jupyter notebook
```

### No Git?

Download as ZIP:
1. Visit [github.com/nishad/llm-workshop-notebooks](https://github.com/nishad/llm-workshop-notebooks)
2. Click "Code" → "Download ZIP"
3. Extract and navigate to folder

---

## Complete Setup Checklist

Verify you have everything:

- [ ] Python 3.8+ installed
- [ ] Virtual environment created and activated
- [ ] `ollama` library installed (0.6.1+)
- [ ] `chromadb` installed
- [ ] `jinja2` installed
- [ ] `jupyter` installed (optional but recommended)
- [ ] Connection test passed
- [ ] Workshop notebooks cloned (optional)

{{< callout type="success" >}}
**Ready to Go!** If all items are checked, you're set up for Part 2 of the workshop.
{{< /callout >}}

---

## Project Structure Suggestion

Organize your workshop files like this:

```
workshop/
├── workshop-env/          # Virtual environment
├── notebooks/             # Jupyter notebooks
├── scripts/               # Python scripts
├── data/                  # Sample data files
└── outputs/               # Generated results
```

---

## Quick Reference

**Activate environment**:
```bash
source workshop-env/bin/activate  # macOS/Linux
workshop-env\Scripts\activate     # Windows
```

**Deactivate environment**:
```bash
deactivate
```

**Install new package**:
```bash
pip install package-name
```

**List installed packages**:
```bash
pip list
```

**Start Jupyter**:
```bash
jupyter notebook
```

---

## Next Steps

Environment set up? Let's start coding!

{{< cards >}}
  {{< card link="/v2/part2-intermediate/01-python-integration/basics" title="Next: Python Basics" icon="arrow-right" subtitle="Learn to generate text, chat, and create embeddings" >}}
{{< /cards >}}
