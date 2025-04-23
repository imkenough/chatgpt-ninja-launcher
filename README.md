# ChatGPT Ninja Launcher

**Formal**: A discreet, hotkey-activated ChatGPT launcher that runs from the system tray. Designed for focus, speed, and zero clutter — this tool gives you instant access to ChatGPT in a Chrome app window that hides when not in use and resumes exactly where you left off.

**Informal**: Launches ChatGPT in a clean Chrome window that doesn’t show on the taskbar. Lives quietly in your system tray. Summon it with a hotkey, hide it instantly with Alt+Tab. Great for multitasking… or, you know, if some teacher walks by. 😉

## Features

- Launches ChatGPT on startup, minimized and hidden from the taskbar
- Keeps your ChatGPT session alive — no process termination
- Hotkey activated (`Ctrl + Shift + Space`)* for quick access          _*editable_
- Auto-hides on focus loss or Alt+Tab
- Packaged as a standalone executable using PyInstaller

## Prefer not to mess with Python?  
👉 [Download Latest Release](https://github.com/imkenough/chatgpt-ninja-launcher/releases/latest)

Just run it — no setup required.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/chatgpt-ninja-launcher.git
   cd chatgpt-ninja-launcher
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the launcher:
   ```bash
   python app.py
   ```

## Building the Executable

To create a standalone `.exe` with PyInstaller:

```bash
pyinstaller --noconfirm --onefile --windowed app.py
```

The final executable will be available in the `dist/` folder.

## Requirements

- Windows OS
- Google Chrome (installed at default path)
- Python 3.7+

## Dependencies

```
pystray
pillow
keyboard
pygetwindow
pywin32
```

## Notes

- This tool uses Chrome in `--app` mode to create a clean, standalone-like window for ChatGPT.
- No session data is lost; the Chrome instance remains running in the background.
- For best results, pin the hotkey app to your startup folder or configure it via Task Scheduler for silent launch at boot.
