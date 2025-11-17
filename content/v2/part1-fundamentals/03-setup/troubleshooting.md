---
title: Troubleshooting
weight: 3
---

## Troubleshooting Common Issues

This guide helps you resolve common problems you might encounter when installing or using Ollama.

### Installation Issues

#### Problem: "App Can't Be Opened" (macOS)

**Symptoms**: macOS shows security warning preventing Ollama from launching

**Solution**:

1. Go to **System Settings** → **Privacy & Security**
2. Scroll down to **Security** section
3. Look for message about Ollama being blocked
4. Click **"Open Anyway"**
5. Confirm by clicking **"Open"** in the dialog

**Alternative**:
```bash
# Remove quarantine attribute
xattr -d com.apple.quarantine /Applications/Ollama.app
```

---

#### Problem: "Windows Protected Your PC" (Windows)

**Symptoms**: SmartScreen prevents installation

**Solution**:

1. Click **"More info"** on the SmartScreen dialog
2. Click **"Run anyway"**
3. Proceed with installation

{{< callout type="info" >}}
**Why This Happens**: New versions of Ollama may not yet have established reputation with SmartScreen. This is safe to bypass for official downloads from ollama.com.
{{< /callout >}}

---

#### Problem: Linux Installation Script Fails

**Symptoms**: `curl: command not found` or permission errors

**Solution**:

Install curl first:

```bash
# Debian/Ubuntu
sudo apt-get update && sudo apt-get install curl

# Fedora/RHEL
sudo dnf install curl

# Arch
sudo pacman -S curl
```

Then run the installation script with proper permissions:

```bash
curl -fsSL https://ollama.com/install.sh | sudo sh
```

---

### Model Download Issues

#### Problem: Download Fails or Stalls

**Symptoms**: Model download stops at a certain percentage or shows errors

**Solutions**:

**1. Check Internet Connection**
```bash
# Test connection to Ollama registry
ping registry.ollama.ai
```

**2. Restart Download**

The download should resume automatically. If not:

CLI Method:
```bash
# Stop Ollama
# macOS/Linux: Find and kill the process
pkill ollama

# Windows: Task Manager → End Ollama process

# Restart and try again
ollama pull llama3.2
```

GUI Method:
- Restart the Ollama application
- Try downloading the model again

**3. Check Disk Space**
```bash
# macOS/Linux
df -h

# Windows
Get-PSDrive C
```

Ensure you have at least 5 GB free before downloading models.

**4. Use Smaller Model**

If the 3B model is too large:
```bash
ollama pull llama3.2:1b
```

This downloads a smaller 1.3 GB model.

---

#### Problem: "Model Not Found" Error

**Symptoms**: Error when trying to run a model

**Solution**:

Verify model is actually downloaded:
```bash
ollama list
```

If not listed, download it:
```bash
ollama pull llama3.2
```

Check for typos in model name:
- ✓ Correct: `llama3.2`
- ✗ Wrong: `llama-3.2`, `llama32`, `llama 3.2`

---

### Performance Issues

#### Problem: Responses Are Very Slow

**Symptoms**: Each word takes 5+ seconds to generate

**Diagnostic Steps**:

1. **Check Available RAM**

   Your system needs enough free RAM for the model:
   - Llama 3.2 (1B): Needs ~3-4 GB available RAM
   - Llama 3.2 (3B): Needs ~4-6 GB available RAM

   ```bash
   # macOS
   vm_stat

   # Linux
   free -h

   # Windows (PowerShell)
   Get-ComputerInfo | Select-Object CsTotalPhysicalMemory, CsNumberOfProcessors
   ```

2. **Close Other Applications**

   Close browser tabs, large applications, etc. to free up RAM

3. **Try Smaller Model**

   Use the 1B variant if the 3B is too slow:
   ```bash
   ollama pull llama3.2:1b
   ```

4. **Check CPU Usage**

   Open Task Manager (Windows) or Activity Monitor (macOS) and verify Ollama is using CPU resources. If CPU usage is very low, there may be a configuration issue.

**Expected Performance Benchmarks**:

| Hardware | Llama 3.2 (1B) | Llama 3.2 (3B) |
|----------|----------------|----------------|
| Apple M1/M2/M3 | 10-30 tokens/sec | 5-15 tokens/sec |
| Modern Intel/AMD (16GB RAM) | 5-15 tokens/sec | 2-8 tokens/sec |
| Minimum Spec (8GB RAM) | 2-8 tokens/sec | 1-4 tokens/sec |

---

#### Problem: Ollama Uses Too Much Memory

**Symptoms**: System becomes sluggish, swap usage is high

**Solution**:

1. **Limit Context Length**

   In GUI settings or via CLI:
   ```bash
   ollama run llama3.2 --ctx-size 2048
   ```

   Reduces memory from default (128K tokens) to 2K tokens

2. **Use Quantized Model**

   The default Llama 3.2 uses Q4_K_M quantization. Verify:
   ```bash
   ollama show llama3.2
   ```

3. **Switch to Smaller Model**
   ```bash
   ollama run llama3.2:1b
   ```

4. **Close and Restart Ollama**

   Sometimes memory isn't released properly. Restart the application.

---

### Connection Issues

#### Problem: CLI Can't Connect to Server

**Symptoms**: `Error: could not connect to ollama server`

**Solutions**:

**1. Verify Ollama is Running**

Check if Ollama process is active:

```bash
# macOS/Linux
ps aux | grep ollama

# Windows (PowerShell)
Get-Process | Where-Object {$_.ProcessName -like "*ollama*"}
```

If not running, start it:

- **GUI**: Launch the Ollama application
- **CLI**: `ollama serve` (runs in foreground)

**2. Check Port 11434**

Ollama listens on port 11434 by default. Verify nothing else is using it:

```bash
# macOS/Linux
lsof -i :11434

# Windows (PowerShell)
netstat -ano | findstr :11434
```

**3. Test Connection**

```bash
curl http://localhost:11434/api/tags
```

Should return a JSON response with available models.

**4. Check Firewall**

Ensure your firewall allows Ollama:
- **macOS**: System Settings → Network → Firewall
- **Windows**: Windows Security → Firewall & network protection
- **Linux**: `sudo ufw status` (if using UFW)

---

#### Problem: GUI Won't Start

**Symptoms**: Ollama icon appears but window doesn't open

**Solutions**:

**1. Reset Ollama**

macOS:
```bash
rm -rf ~/.ollama/logs
killall Ollama
open -a Ollama
```

Windows:
```powershell
Remove-Item -Recurse $env:USERPROFILE\.ollama\logs
taskkill /F /IM ollama.exe
Start-Process "C:\Users\[YourName]\AppData\Local\Programs\Ollama\Ollama.exe"
```

**2. Check Logs**

macOS/Linux:
```bash
cat ~/.ollama/logs/server.log
```

Windows:
```powershell
Get-Content $env:USERPROFILE\.ollama\logs\server.log
```

Look for error messages indicating the problem.

**3. Reinstall Ollama**

As a last resort:
1. Uninstall Ollama
2. Delete data directory (`~/.ollama` or `%USERPROFILE%\.ollama`)
3. Reinstall from ollama.com
4. Re-download models

{{< callout type="warning" >}}
**Backup First**: Deleting `~/.ollama` removes all downloaded models. You'll need to re-download them (2-5 GB per model).
{{< /callout >}}

---

### Model Quality Issues

#### Problem: Responses Are Nonsensical or Repetitive

**Symptoms**: Model outputs gibberish, repeats phrases, or provides irrelevant answers

**Solutions**:

**1. Adjust Temperature**

Try lowering temperature for more focused responses:

GUI: Settings → Temperature → Set to 0.5-0.7

CLI:
```bash
ollama run llama3.2 --temperature 0.6
```

**2. Reset Context**

Sometimes the context becomes corrupted:

- **GUI**: Start a new conversation (new chat button)
- **CLI**: Exit (`/bye`) and restart (`ollama run llama3.2`)

**3. Verify Model Integrity**

Re-download the model:
```bash
ollama rm llama3.2
ollama pull llama3.2
```

**4. Check Quantization**

Default Q4_K_M should work well. If quality is poor, try higher quantization:
```bash
ollama pull llama3.2:q5_k_m
```

---

### Python Integration Issues

(For Part 2 of the workshop)

#### Problem: `ollama` Python Library Not Found

**Symptoms**: `ModuleNotFoundError: No module named 'ollama'`

**Solution**:

Install the library:
```bash
pip install ollama
```

Or with specific Python version:
```bash
python3 -m pip install ollama
```

---

#### Problem: Python Can't Connect to Ollama

**Symptoms**: Connection errors in Python scripts

**Solution**:

Ensure Ollama server is running:
```python
import ollama

# Test connection
try:
    ollama.list()
    print("Connected successfully!")
except Exception as e:
    print(f"Connection failed: {e}")
```

If connection fails:
1. Start Ollama application
2. Or run `ollama serve` in terminal
3. Verify port 11434 is accessible

---

### Getting More Help

If your issue isn't covered here:

1. **Check Official Documentation**: [ollama.com/docs](https://ollama.com/docs)
2. **GitHub Issues**: [github.com/ollama/ollama/issues](https://github.com/ollama/ollama/issues)
3. **Community Discord**: Join Ollama Discord for community support
4. **During Workshop**: Ask questions in Zoom chat or raise your hand

### Diagnostic Information

When seeking help, provide:

```bash
# Ollama version
ollama --version

# System info
# macOS
system_profiler SPSoftwareDataType SPHardwareDataType

# Linux
uname -a && lsb_release -a

# Windows (PowerShell)
Get-ComputerInfo | Select-Object OsName, OsVersion, CsProcessors, CsTotalPhysicalMemory

# List models
ollama list

# Check logs
cat ~/.ollama/logs/server.log  # macOS/Linux
Get-Content $env:USERPROFILE\.ollama\logs\server.log  # Windows
```

This information helps diagnose issues quickly.

---

{{< callout type="success" >}}
**Most Issues Are Easily Fixable**: Don't get discouraged! The majority of problems are simple permission, connection, or resource issues that can be resolved in minutes.
{{< /callout >}}

### Return to Setup

{{< cards >}}
  {{< card link="/v2/part1-fundamentals/03-setup" title="Back to Setup Overview" icon="arrow-left" >}}
  {{< card link="/v2/part1-fundamentals/03-setup/first-chat" title="Continue to First Chat" icon="arrow-right" >}}
{{< /cards >}}
