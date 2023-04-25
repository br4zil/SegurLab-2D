import tkinter as tk
from tkinter import filedialog
import sys

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

text_file = open("config.txt", "w")
n = text_file.write(file_path)
text_file.close()
