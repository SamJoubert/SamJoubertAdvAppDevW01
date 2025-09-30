# Program Name: A3.py
# Course: IT3883/Section W01
# Student Name: Sam Joubert
# Assignment Number: Lab 3
# Due Date: 10/05/2025
# Purpose: This program simply converts miles per gallon to kilometers per liter. However,
# it will be in a user friendly GUI environment as opposed to a python output panel, and will
# update automatically as users type in numbers.
# List Specific resources used to complete the assignment: Module 3-2 GUI, W3Schools
# Python Functions, W3Schools Python String format() Method

import tkinter as tk

#conversion factor from mpg to km/l
mpg_to_kmpl = 0.425144

#function which converts numeric input and gives no output for non-numeric input
def convert(*args):
    try:
        mpg = float(entry.get())
        kmpl = mpg * mpg_to_kmpl
        result_var.set(f"{kmpl:.2f} km/l") #rounds to the hundredths place to save space
    except ValueError:
        result_var.set("")

#creates main application window
root = tk.Tk()
root.title("MPG to KM/L Converter")

#creates and places widgets
tk.Label(root, text="Miles per Gallon (MPG):").grid(row=0, column=0, pady=10)

entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10)
entry.bind("<KeyRelease>", convert)  #recalculates on every keypress

tk.Label(root, text="Kilometers per Liter (KM/L):").grid(row=1, column=0, padx=10, pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, fg="blue")
result_label.grid(row=1, column=1, pady=10)

#starts the GUI event loop
root.mainloop()
