#MADE BY MRCAT
import time
import webbrowser
from playsound import playsound
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import os

webbrowser.open ("https://media.tenor.com/jeYb8iK3YfsAAAAi/skull-skullgif.gif")
audio_file = "yeah.mp3"
playsound(audio_file)
time.sleep(1)
webbrowser.open ("https://duckduckgo.com/?t=ffab&q=elmo+feet+pics&ia=web")
time.sleep(4)
webbrowser.open ("https://duckduckgo.com/?t=ffab&q=sans+x+paapyrus+ship&iax=images&iai=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F60%2Fa1%2Fb9%2F60a1b9331c2b9f746b6dc680d5fd6c0e.png&ia=images")
time.sleep(4)
webbrowser.open ("https://www.youtube.com/watch?v=QqHqP_yVCRY")

time.sleep(23)
webbrowser.open ("https://www.youtube.com/watch?v=KcPFKKu49sc")
time.sleep(10)
webbrowser.open ("https://www.youtube.com/watch?v=VJT1NA38tJ8")

time.sleep(12)
webbrowser.open ("https://www.youtube.com/watch?v=ksKAgbFDyUU")
time.sleep(23)
webbrowser.open ("https://www.youtube.com/watch?v=2-H7DVE8_PM")
time.sleep(18)
webbrowser.open ("https://www.youtube.com/watch?v=b4XpMTUlorc")
time.sleep(20)
webbrowser.open ("https://www.youtube.com/watch?v=XsAI0RqoiTA")
time.sleep(4)
webbrowser.open ("https://www.youtube.com/watch?v=bNy341mHHjs")
time.sleep (5)

root = tk.Tk()
root.withdraw()  # Hide the main window

# Load the image
image = Image.open("scared.jpg")

# Convert the image to Tkinter PhotoImage format
tk_image = ImageTk.PhotoImage(image)

# Create a new window for the image
image_window = tk.Toplevel(root)
image_window.title("Image Display")

# Create a label to display the image
label = tk.Label(image_window, image=tk_image)
label.image = tk_image  # Keep a reference to the image to prevent it from being garbage collected
label.pack()

response = messagebox.askyesno("Last message.", "Ready for death?")

if response:
    # Run the tkinter event loop for the image window
    image_window.mainloop()

time.sleep(1)
os.system("shutdown /s /t 30")
