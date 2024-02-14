# It doesn't work on WSL2 Windows for problems gnome capturer!!!!!!!!!!!!


import time
import tkinter as tk

# import pyautogui


def screenshot():
    name = int(round(time.time() * 1000))
    name = "/home/ahinojosa/formacion/20-python-projects/screenshots/{}.png".format(
        name
    )
    print("Screenshot saved at:", name)
    # time.sleep(5)
    # img = pyautogui.screenshot("name")
    # img.show()


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, text="Text a screenshot", command=screenshot)
button.pack(side=tk.LEFT)

close = tk.Button(frame, text="Quit", command=quit)
close.pack(side=tk.LEFT)

root.mainloop()
