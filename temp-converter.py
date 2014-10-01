#!/usr/bin/python3
# feedback_template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

class Converter:

    def __init__(self, master):
        self.master = master
        master.title("Temperature Converter")
        master.geometry("215x145")

        self.cellabel = ttk.Label(master, text = "Celsius:", anchor=W, justify=LEFT)
        self.cellabel.grid(row=0,column=0)

        self.tempC = ttk.Entry(master, width = 25)
        self.tempC.grid(row=1, column=0, columnspan = 2, padx=5)

        self.fahlabel = ttk.Label(master, text = "Fahrenheit:")
        self.fahlabel.config(justify = LEFT)
        self.fahlabel.grid(row=2, column=0)

        self.tempF = ttk.Entry(master, width = 25)
        self.tempF.grid(row=3, column=0, columnspan=2)

        self.btnConv = ttk.Button(master, text = "Convert", command= self.convert).grid(row=4, column=0, padx=5,pady=5)
        self.btnClear= ttk.Button(master, text = "Clear", command= self.clear).grid(row=4, column=1, padx=5,pady=5)
        self.btnquit= ttk.Button(master, text = "Quit", command= self.quit).grid(row=5, column=0, columnspan = 2)



    def convert(self):
        if self.tempC.get( ) :
            try:
                self.numC = float(self.tempC.get( ))
                self.numF = (self.numC * (9/5)) + 32
                self.tempF.insert(0,str(self.numF))
            except ValueError:
                showwarning("Warning","Please enter a number and not a letter!")
                self.tempC.delete(0, 'end')
        elif self.tempF.get() :
            try:
                self.numF = float(self.tempF.get( ))
                self.numC = (self.numF - 32) * (5/9)
                self.tempC.insert(0,str(self.numC))
            except ValueError:
                showwarning("Warning","Please enter a number and not a letter!")
                self.tempF.delete(0, 'end')

    def clear(self):
        self.tempF.delete(0, 'end')
        self.tempC.delete(0, 'end')

    def quit(self):
        self.master.destroy()

def main():

    root = Tk()
    converter = Converter(root)
    root.mainloop()

if __name__ == "__main__": main()
