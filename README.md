# ChatGPT Ninja

A lightweight Windows utility to launch and manage ChatGPT in an isolated, minimal browser window directly from the system tray.

[Blog Post](https://imkenough.ddnsfree.com/blog/chatgpt-ninja-launcher)

## Overview

**ChatGPT Ninja** is a simple background application that launches ChatGPT in a dedicated Chrome app window (incognito mode), automatically hides it from the desktop view, and allows users to bring it to the foreground with a customizable hotkey (`Ctrl + Shift + Space`).

The app quietly runs from the system tray, providing quick access to ChatGPT without cluttering the taskbar or desktop environment.

## Features

- **Hidden Window Management**: Launch ChatGPT in an incognito Chrome app window, hidden by default.
- **Global Hotkey Activation**: Instantly bring the ChatGPT window to the foreground using `Ctrl + Shift + Space`.
- **System Tray Integration**: Easily show, hide, or quit the application from the system tray.
- **Auto-Center and Resize**: Ensures a consistent and clean window position and size every time.
- **Lightweight and Minimal**: Designed for low resource usage and minimal user distraction.
- **Standalone EXE Build**: Easily build a versioned standalone executable file for Windows.

## Installation

#### Prefer not to mess with the code?
[Download](https://github.com/imkenough/chatgpt-ninja-launcher/releases/latest) the latest release .exe 

### Clone the Repository
First, clone the repository:

```bash
git clone https://github.com/imkenough/chatgpt-ninja-launcher
cd chatgpt-ninja-launcher
```


### Prerequisites
- **Python 3.8+** (only if running from source)
- **Google Chrome** installed at:
  `C:\Program Files\Google\Chrome\Application\chrome.exe`
- **Virtual enviroment setup** (preferably)
  

### Python Dependencies
Install required libraries:
```bash
pip install -r requirements.txt
```
or
```bash
pip install pystray pillow pywin32 keyboard
```


## Usage

### Running from Source
1. Ensure all dependencies are installed.
2. Run the application:
   ```bash
   python appCnl.py
   ```

### Hotkeys and Tray Menu
| Function             | Shortcut / Action |
|:---------------------|:------------------|
| Show ChatGPT          | `Ctrl + Shift + Space` or System Tray → "Show ChatGPT" |
| Quit Application      | System Tray → "Quit" |

The ChatGPT window will automatically hide when focus is lost.

## Building the Executable (Optional)

The repository includes a `build.py` script that uses PyInstaller to create a standalone `.exe`.

### Steps:
1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Create a `version.txt` file with your desired version (e.g., `v1.0.0`).
3. Build the executable:
   ```bash
   python build.py
   ```

The final executable will be available in the `/dist` directory, named based on the version (e.g., `cnl_v1.0.0.exe`).

## Project Structure

```
├── appCnl.py          # Main application script
├── build.py           # Build script for generating the EXE
├── version.txt        # Version information
├── icon.png           # (Optional) Icon for system tray
├── icon.ico           # (Optional) Icon for the exe
├── dist/              # Output folder for built executable
├── specs/             # PyInstaller spec files
```

## Acknowledgements

- Developed by [imkenough](https://github.com/imkenough).
- Powered by Python, PyInstaller, and various Windows APIs.
