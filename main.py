import tkinter as tk
import random
import threading
import os
import sys
import ctypes

# Hide the console window (Windows only)
if os.name == 'nt':
    ctypes.windll.kernel32.GetConsoleWindow()
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

# Opens small windows
def open_window():
    window = tk.Tk()
    window.title("Warning")
    label = tk.Label(window, text="You have been pranked!", font=("Arial", 20)) #Change to desired text
    label.pack(padx=50, pady=50)
    window.geometry("400x200")
    window.mainloop()

# Color FLASHING
def flash_screen():
    while True:
        color = random.choice(["red", "green", "blue", "yellow", "purple", "cyan", "orange"])
        root.configure(bg=color)
        time.sleep(0.5)  # Delay between color changes

# Create X amount of windows
for _ in range(50): #Change to how many windows you want to open
    threading.Thread(target=open_window, daemon=True).start()

root = tk.Tk()
root.geometry("400x400")  # Sets window size
root.attributes("-fullscreen", True)  # Makes the window fullscreen

# Colors
colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink', 'cyan']

# Color BLINKING
def blink():
    color = random.choice(colors) 
    root.configure(bg=color) 
    root.after(25, blink)

blink()

root.mainloop()
