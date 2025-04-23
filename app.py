import subprocess
import threading
import time
import win32gui
import pythoncom
import win32con
import win32api
import win32com.client
import win32process
import keyboard
from pystray import Icon, MenuItem, Menu
from PIL import Image
import os

# --- Global state ---
window_handle = None
chatgpt_launched = False

def on_quit(icon, item):
    icon.stop()
    os._exit(0)

def on_show(icon, item):
    global window_handle
    if window_handle:
        show_window(window_handle)

def create_icon():
    icon_image = Image.new('RGB', (64, 64), color=(0, 0, 0))
    return Icon("ChatGPT Ninja", icon_image, menu=Menu(
        MenuItem("Show ChatGPT", on_show),
        MenuItem("Quit", on_quit)
    ))

def hide_window(hwnd):
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
    ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, ex_style | win32con.WS_EX_TOOLWINDOW)

import win32process  # already imported, just confirming

def show_window(hwnd):
    try:
        pythoncom.CoInitialize()
        shell = win32com.client.Dispatch("WScript.Shell")

        # Step 1: Show and restore window
        win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

        # Step 2: Send ALT key to reset focus lock
        shell.SendKeys('%')
        time.sleep(0.1)

        # Step 3: Minimize and restore if still not focused (force Z-order bump)
        win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
        time.sleep(0.1)
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)

        # Step 4: Try again to focus
        win32gui.SetForegroundWindow(hwnd)

    except Exception as e:
        print(f"Could not bring window to front: {e}")           

def resize_and_center_window(hwnd, width=900, height=600):
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    win32gui.MoveWindow(hwnd, x, y, width, height, True)

def launch_chatgpt(hidden=True):
    global window_handle, chatgpt_launched

    if chatgpt_launched:
        return  # Don't launch again

    subprocess.Popen([
        "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
        "--incognito",
        "--app=https://chat.openai.com"
    ])
    chatgpt_launched = True

    time.sleep(2.5)

    def enum_callback(hwnd, result):
        title = win32gui.GetWindowText(hwnd)
        if "chatgpt" in title.lower() or "chat.openai" in title.lower():
            result.append(hwnd)

    results = []
    win32gui.EnumWindows(enum_callback, results)

    if results:
        window_handle = results[0]
        resize_and_center_window(window_handle, width=800, height=650)
        if hidden:
            hide_window(window_handle)
        else:
            show_window(window_handle)

def monitor_focus():
    global window_handle
    while True:
        if window_handle:
            try:
                fg = win32gui.GetForegroundWindow()
                if fg != window_handle:
                    hide_window(window_handle)
            except Exception as e:
                print(f"Focus check error: {e}")
        time.sleep(0.3)

def keybind_listener():
    global window_handle
    keyboard.add_hotkey('ctrl+shift+space', lambda: show_window(window_handle) if window_handle else None)
    keyboard.wait()

def main():
    launch_chatgpt(hidden=True)  # 🔥 Launches at start, already hidden
    tray_icon = create_icon()
    threading.Thread(target=keybind_listener, daemon=True).start()
    threading.Thread(target=monitor_focus, daemon=True).start()
    tray_icon.run()

if __name__ == "__main__":
    main()
