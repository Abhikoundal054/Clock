import time
from tkinter import *
root = Tk()
root.geometry("400x100+940+100")
root.wm_iconbitmap("clock.ico")
# root.overrideredirect(1)
root.title("Clock")
root.config(background ="black")

def start():
    label.config(text=time.strftime("%H:%M:%S %p"))
    label.after(200,start)

label=Label(root,font=("lucida",50,"bold"),bg="black",fg ="red")
label.pack()
start()
print("syatem is secure\n Clock is displayed")
root.mainloop()