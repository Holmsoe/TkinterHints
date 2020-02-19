#from tkinter import *

import tkinter as tk
master = tk.Tk()

mincanvas = tk.Canvas(master, width=400, height=400)

#Farver
# http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter

#Rectangle
mincanvas.create_rectangle(50, 25, 150, 75, activefill="red",fill="khaki3",outline="blue")
mincanvas.create_text(50,100,text="Min tekst")
mincanvas.create_oval(50,150,150,300)
mincanvas.create_polygon(250,50,300,150,200,200,300,300)

widget = tk.Label(mincanvas, text='Spam', fg='white', bg='black')
widget.pack()

mincanvas.create_window(180, 180, window=widget) 


mincanvas.pack()
mincanvas.mainloop()

