"""
Try to configure the widget with various options like:
bg=”red”, family=”times”, size=18
"""

from tkinter import *

root = Tk()
root.title("Welcome to GeekForGeeks") 
root.geometry("400x240")

a = Label(root, text ="Hello World",bg="red",font=("times",18))
a.pack()
  
root.mainloop()
