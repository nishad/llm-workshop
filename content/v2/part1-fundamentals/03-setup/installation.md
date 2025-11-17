---
title: Installing Ollama
weight: 1
---

## Installing Ollama GUI

This page walks you through downloading and installing Ollama with its native GUI interface.

### Step 1: Download Ollama

Visit the official Ollama download page:

**👉 [ollama.com/download](https://ollama.com/download)**

Select your operating system and download the installer.

{{< callout type="warning" >}}
**Important**: Download only from the official Ollama website (ollama.com) to ensure you get the authentic, safe version.
{{< /callout >}}

---

### Step 2: Install on Your Operating System

The installation process varies slightly by platform:

{{< tabs items="macOS,Windows,Linux" >}}

{{< tab >}}
### macOS Installation

1. **Download the .dmg file** from ollama.com/download

2. **Open the downloaded .dmg file**

   Double-click `Ollama-[version].dmg` in your Downloads folder

3. **Drag Ollama to Applications**

   A window will appear showing the Ollama icon and your Applications folder. Drag the Ollama icon to the Applications folder.

4. **Launch Ollama**

   - Open your Applications folder
   - Double-click the Ollama icon
   - If you see a security warning, click "Open" to confirm

5. **Grant Permissions** (if prompted)

   macOS may ask for permissions to run Ollama. Click "OK" or "Allow" to grant necessary permissions.

{{< callout type="info" >}}
**First Launch**: On first launch, macOS may take a few seconds to verify the application. This is normal.
{{< /callout >}}

{{< /tab >}}

{{< tab >}}
### Windows Installation

1. **Download the .exe installer** from ollama.com/download

2. **Run the installer**

   Double-click `OllamaSetup.exe` in your Downloads folder

3. **User Account Control (UAC) prompt**

   Windows will ask if you want to allow the app to make changes. Click "Yes"

4. **Follow the installation wizard**

   - Click "Next" to begin
   - Choose installation location (default is recommended)
   - Click "Install"
   - Wait for installation to complete

5. **Launch Ollama**

   - The installer will offer to launch Ollama automatically
   - Or find Ollama in your Start Menu

{{< callout type="info" >}}
**Installation Location**: Ollama installs to `C:\Users\[YourName]\AppData\Local\Programs\Ollama` by default. The models will be stored in `C:\Users\[YourName]\.ollama\models`.
{{< /callout >}}

{{< /tab >}}

{{< tab >}}
### Linux Installation

{{< callout type="warning" >}}
**Note**: As of 2025, Ollama's native GUI is available only for macOS and Windows. Linux users should use the CLI with a web-based interface like Open WebUI or ChatBox.
{{< /callout >}}

1. **Install Ollama CLI**

   Run the official installation script:

   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

2. **Verify installation**

   ```bash
   ollama --version
   ```

3. **Start Ollama service**

   ```bash
   ollama serve
   ```

   This starts Ollama as a background service on `http://localhost:11434`

4. **(Optional) Install a GUI Alternative**

   For a GUI experience on Linux, consider:

   - **Open WebUI**: Web-based interface
     ```bash
     docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway \
       -v open-webui:/app/backend/data --name open-webui --restart always \
       ghcr.io/open-webui/open-webui:main
     ```

   - **[ChatBox](https://chatboxai.app/en)**: Desktop application for Linux GUI

{{< /tab >}}

{{< /tabs >}}

---

### Step 3: Verify Installation

After installation, verify that Ollama is running:

#### Using the GUI (macOS/Windows)

1. **Look for the Ollama icon** in your system tray (Windows) or menu bar (macOS)

2. **Click the icon** to open the Ollama window

3. **Check the interface**

   You should see the Ollama chat interface with a welcome message

#### Using the CLI (All Platforms)

Open Terminal (macOS/Linux) or Command Prompt (Windows) and run:

```bash
ollama --version
```

Expected output:
```
ollama version is 0.10.0 (or later)
```

{{< callout type="success" >}}
**Success!** If you see the version number, Ollama is installed correctly.
{{< /callout >}}

---

### Step 4: Understanding the Ollama Interface

Once installed, Ollama provides two main interfaces:

#### GUI Interface (Recommended for Beginners)

The native Ollama GUI includes:

- **Chat Window**: Main area for conversations
- **New Chat Button**: Start fresh conversations
- **Model Selector**: Dropdown at the bottom to choose and download models
- **Message Input**: "Send a message" box at the bottom
- **Attachment Support**: Add files to your conversations (+ button)

#### CLI Interface (For Advanced Users)

The command-line interface allows you to:

```bash
ollama list                    # List installed models
ollama pull llama3.2          # Download a model
ollama run llama3.2           # Start chatting with a model
ollama rm llama3.2            # Remove a model
ollama serve                  # Start Ollama server
```

---

### What's Next?

Now that Ollama is installed, let's download a model and start chatting:

{{< cards >}}
  {{< card link="/v2/part1-fundamentals/03-setup/first-chat" title="Next: First Chat" icon="arrow-right" subtitle="Download Llama 3.2 and start your first conversation" >}}
{{< /cards >}}

### Having Issues?

If installation didn't work, check the [Troubleshooting](/v2/part1-fundamentals/03-setup/troubleshooting) guide.
