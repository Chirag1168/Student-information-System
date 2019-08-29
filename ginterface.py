import Tkinter
import tkMessageBox
def display1():
    tkMessageBox.showinfo("result","character user interface")
def display2():
    tkMessageBox.showinfo("result","graphical user interface")
top=Tkinter.Tk()
b1=Tkinter.Button(top,text="CUI",command=display1)
b1.pack(side=Tkinter.LEFT)
b2=Tkinter.Tk()
    
