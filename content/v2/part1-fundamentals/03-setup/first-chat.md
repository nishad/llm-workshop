---
title: Your First Chat
weight: 2
---

## Starting Your First Conversation with Llama 3.2

Now that Ollama is installed, let's download a model and start chatting!

### Step 1: Download Llama 3.2

Llama 3.2 is our primary model for this workshop. It's efficient, capable, and runs well on consumer hardware.

{{< tabs items="GUI Method,CLI Method" >}}

{{< tab >}}
### Using the Ollama GUI

1. **Open the Ollama application**

2. **Click the Model Selector dropdown** at the bottom of the window

   You'll see the current model name (or "Find model...") in a dropdown button.

   ![Ollama GUI Model Selection](/images/setup/ollama-gui.png)

3. **Search for "llama3.2"** in the "Find model..." search box

   Type "llama3.2" in the search field that appears

4. **Select and download "llama3.2:3b"**

   You'll see options like:
   - `llama3.2:1b` (smaller, faster)
   - `llama3.2:3b` (recommended for workshop)

   Click the download icon (↓) next to `llama3.2:3b` to download it.

5. **Wait for download to complete**

   Download size: ~2 GB for the 3B version
   Time: 5-15 minutes depending on your internet speed

   The download icon will change to indicate when the model is ready.

{{< callout type="info" >}}
**During Download**: You can leave Ollama running in the background. The download will continue even if you minimize the window.
{{< /callout >}}

{{< /tab >}}

{{< tab >}}
### Using the Command Line

Open your terminal (macOS/Linux) or Command Prompt (Windows) and run:

```bash
ollama pull llama3.2
```

You'll see output like:

```
pulling manifest
pulling 8eeb52dfb3bb... 100% ▕████████████████▏ 2.0 GB
pulling 73b313b5552d... 100% ▕████████████████▏  120 B
pulling 0ba8f0e314b4... 100% ▕████████████████▏  483 B
verifying sha256 digest
writing manifest
removing any unused layers
success
```

**Alternative: Download the 1B version** (if you have limited RAM):

```bash
ollama pull llama3.2:1b
```

{{< /tab >}}

{{< /tabs >}}

---

### Step 2: Verify the Model Downloaded

Let's confirm the model is ready to use.

#### GUI Method

1. **Click the model selector dropdown** at the bottom of the window

2. **Verify llama3.2 appears** in the list

   After download completes, `llama3.2:3b` (or `llama3.2:1b`) should appear in the model list without a download icon next to it

#### CLI Method

```bash
ollama list
```

Expected output:

```
NAME              ID              SIZE      MODIFIED
llama3.2:latest   8eeb52dfb3bb    2.0 GB    2 minutes ago
```

{{< callout type="success" >}}
**Great!** Your model is downloaded and ready. Let's start chatting!
{{< /callout >}}

---

### Step 3: Your First Conversation

Now for the exciting part - talking to your local LLM!

{{< tabs items="GUI Chat,CLI Chat" >}}

{{< tab >}}
### Using the Ollama GUI

1. **Select llama3.2:3b** from the model dropdown at the bottom of the window

   Click the dropdown button and choose `llama3.2:3b` from the list

2. **Type a message in the "Send a message" input box**

   Try this simple prompt:
   ```
   Hello! Please introduce yourself and tell me what you can help with.
   ```

3. **Press Enter or click the Send button (↑)**

4. **Watch the response generate**

   You'll see the model's response appear in the chat area in real-time (streaming)

**Expected Response** (may vary):

```
Hello! I'm Llama, a large language model trained by Meta AI. I'm here to
assist you with a wide variety of tasks, including:

- Answering questions on various topics
- Generating text and creative content
- Helping with writing, editing, and proofreading
- Providing information and explanations
- Assisting with problem-solving and brainstorming
- And much more!

I'm running locally on your machine, which means your conversations stay
private and don't require an internet connection. How can I help you today?
```

{{< /tab >}}

{{< tab >}}
### Using the CLI

Start an interactive chat session:

```bash
ollama run llama3.2
```

You'll see a prompt:

```
>>>
```

Type your message and press Enter:

```
>>> Hello! Please introduce yourself and tell me what you can help with.
```

The model will respond directly in the terminal.

**CLI Commands**:
- Type your messages and press Enter
- Use `/bye` to exit
- Use `Ctrl+D` to exit
- Scroll up to see conversation history

{{< /tab >}}

{{< /tabs >}}

---

### Step 4: Experiment with Basic Prompts

Try these prompts to get familiar with your local LLM:

#### Factual Question
```
What are the three laws of thermodynamics?
```

#### Creative Task
```
Write a haiku about local AI running on personal computers.
```

#### Coding Help
```
Write a Python function to check if a number is prime.
```

#### Explanation
```
Explain machine learning to a 10-year-old.
```

#### Translation
```
Translate "Hello, how are you?" to Spanish, French, and German.
```

{{< callout type="info" >}}
**Observe**: Notice how the model responds differently to different types of prompts. We'll explore prompting techniques in depth in the next section.
{{< /callout >}}

---

### Step 5: Understanding the Interface

The Ollama GUI provides a clean, simple interface:

#### Main Interface Elements

- **New Chat button** (top left): Start a fresh conversation
- **Model selector** (bottom): Choose which model to use
- **Send button (↑)**: Submit your message
- **Attachment button (+)**: Add files to your conversation (if supported)
- **Globe icon**: Language or network settings

{{< callout type="info" >}}
**Advanced Settings**: For fine-tuning model parameters like temperature and context length, you'll typically need to use the CLI or API. The GUI focuses on simplicity and ease of use.
{{< /callout >}}

---

### Step 6: Upload Files (Optional - If Supported)

If your Ollama GUI version supports file uploads:

1. **Drag and drop a text file** into the chat window

2. **Ask questions about the file**:

   ```
   Summarize this document in 3 bullet points.
   ```

   ```
   What are the main themes in this text?
   ```

{{< callout type="warning" >}}
**File Support**: File upload features may vary by Ollama version. If not available in GUI, we'll cover file processing with Python in Part 2.
{{< /callout >}}

---

### Understanding What Just Happened

Congratulations! You just:

✓ Downloaded a 3-billion-parameter language model to your computer
✓ Ran it entirely locally (no cloud services)
✓ Had conversations that stayed completely private
✓ Experimented with different types of prompts

**Key Points**:

1. **Everything is Local**: The model runs on your CPU/GPU, using your RAM
2. **Privacy**: No data leaves your computer
3. **Offline Capable**: Works without internet (after model download)
4. **Free**: No per-use costs or subscriptions
5. **Customizable**: You control all settings and behavior

---

### Common Questions

**Q: How fast should responses be?**

**A:** It varies by hardware:
- **Fast** (< 1 second per word): Modern Apple Silicon, high-end GPUs
- **Medium** (1-3 seconds per word): Recent CPUs with 16+ GB RAM
- **Slower** (3-5 seconds per word): Older hardware, minimum specs

Speed is acceptable as long as responses are coherent and useful.

**Q: Can I run multiple models?**

**A:** Yes! Download more models with `ollama pull [model-name]`. Switch between them in the GUI dropdown or CLI.

**Q: How much memory does it use?**

**A:** Llama 3.2:
- `1b` model: ~1.5 GB RAM
- `3b` model (default): ~2.5 GB RAM
- Plus overhead: ~1-2 GB

On an 8 GB system, the 3B model should run comfortably.

---

### Next Steps

Now that you can chat with your local LLM, let's learn how to get better results through effective prompting:

{{< cards >}}
  {{< card link="/v2/part1-fundamentals/04-prompting" title="Next: Prompting Techniques" icon="arrow-right" subtitle="Learn to write effective prompts for better results" >}}
{{< /cards >}}

### Troubleshooting

If you encountered any issues:

{{< cards >}}
  {{< card link="/v2/part1-fundamentals/03-setup/troubleshooting" title="Troubleshooting Guide" icon="cog" subtitle="Solutions to common problems" >}}
{{< /cards >}}
