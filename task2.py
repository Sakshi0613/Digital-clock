import time
from tkinter import *

root = Tk()
root.geometry("500x250+0+0")

root.configure(background="white")
root.resizable(0,0)
root.overrideredirect(0)
def start():
    text=time.strftime("%H:%M:%S")
    label.config(text=text)
    label.after(200,start)
label=Label(root,font=("ds-digital",75,'bold'),bg="white",fg="black",bd=50)
label.grid(row=0,column=1)
start()
print("Digital clock executed!!")
root.mainloop()