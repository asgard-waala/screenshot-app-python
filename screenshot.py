import time
import pyautogui
import tkinter as tk

def screenshot():
    name = str(round(time.time()))
    name = '{}.png'.format(name)
    print(name)
    image = pyautogui.screenshot(name)
    image.show()

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

frame.master.title("Screenshot")
button = tk.Button(
    frame,
    text="Take Screenshot",
    command=screenshot
)

button.pack(side=tk.LEFT)
close_button = tk.Button(
    frame,
    text="Close",
    command=quit
)

close_button.pack(side=tk.RIGHT)
root.mainloop()