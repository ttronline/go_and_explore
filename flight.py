#This Program is made with Tkinter Package

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("GO AND EXPLORE APPLICATION")
root.geometry("500x200")

label = ttk.Label(root, text="GO AND EXPLORE")
label.pack()

n = tk.StringVar()
cbox = ttk.Combobox(root, width = 27, textvariable = n)
cbox.pack()
def click():
  airway = cbox.get()
  airplane = f"You have selected {airway}"
  my_lab = ttk.Label(text=airplane)
  my_lab.pack()

btn = ttk.Button(root, text="Submit", command=click)
btn.pack()
flights = ["Indigo", "SpiceJet", "AirAsia", "Vistara", "Air India","Boeing"]
cbox['values'] = flights


root.mainloop()

