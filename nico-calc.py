#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 19:57:59 2019

@author: nico
"""

from tkinter import *

root = Tk()
root.title("Simple calculator")


cuadro = Entry(root, width=25, borderwidth=3)
cuadro.grid(row=0, column=0, columnspan=6, padx=10, pady=10)








def button_click(number):
     
     current = cuadro.get()
     cuadro.delete(0, END)
     cuadro.insert(0, str(current) + str(number))
     
def button_clear():
     cuadro.delete(0, END)
     
def button_add():
     first_number = cuadro.get()     
     global f_num
     global math
     math = "addition" 
     f_num = int(first_number)
     cuadro.delete(0, END)


def button_menos():
     first_number = cuadro.get()     
     global f_num
     global math
     math = "menos" 
     f_num = int(first_number)
     cuadro.delete(0, END)
     

def button_multiplicar():
     first_number = cuadro.get()     
     global f_num
     global math
     math = "multiplicar" 
     f_num = int(first_number)
     cuadro.delete(0, END)

def button_dividir():
     first_number = cuadro.get()     
     global f_num
     global math
     math = "dividir" 
     f_num = int(first_number)
     cuadro.delete(0, END)

def button_equal():
     second_number = cuadro.get()
     cuadro.delete(0, END)
     
     if math == "addition":
          cuadro.insert(0, f_num + int(second_number))

     if math == "menos":
          cuadro.insert(0, f_num - int(second_number))

     if math == "multiplicar":
          cuadro.insert(0, f_num * int(second_number))

     if math == "dividir":
          cuadro.insert(0, f_num / int(second_number))


button_1 = Button(root, text = "1", padx=20, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text = "2", padx=20, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text = "3", padx=20, pady=20, command=lambda: button_click(3))

button_4 = Button(root, text = "4", padx=20, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text = "5", padx=20, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text = "6", padx=20, pady=20, command=lambda: button_click(6))

button_7 = Button(root, text = "7", padx=20, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text = "8", padx=20, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text = "9", padx=20, pady=20, command=lambda: button_click(9))

button_0 = Button(root, text = "0", padx=20, pady=20, command=lambda: button_click(0))
button_equal = Button(root, text = "=", padx=20, pady=20, command=button_equal)
button_clear = Button(root, text = "clear", padx=10, pady=20, command=button_clear)

button_add = Button(root, text = "+", padx=20, pady=20, command=button_add)
button_menos = Button(root, text = "-", padx=23, pady=20, command=button_menos)
button_multiplicar = Button(root, text = "*", padx=23, pady=20, command=button_multiplicar)
button_dividir = Button(root, text = "/", padx=23, pady=20, command=button_dividir)





button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_add.grid(row=4, column=3)
button_menos.grid(row=3, column=3)
button_multiplicar.grid(row=2, column=3)
button_dividir.grid(row=1, column=3)











root.mainloop()