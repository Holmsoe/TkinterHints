import tkinter as tk

mitVindue = tk.Tk()

mincanvas = tk.Canvas(mitVindue, width=400, height=400, bg="yellow")
mincanvas.pack()
#Farver
# http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter

#Rectangle
mincanvas.create_rectangle(50, 25, 150, 75, activefill="red",fill="khaki3",outline="blue")
mincanvas.create_text(50,100,text="Min tekst")
mincanvas.create_oval(50,150,150,300)
mincanvas.create_polygon(250,50,300,150,200,200,300,300)
mincanvas.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
mincanvas.create_arc(100,200,150,300)

i = mincanvas.create_line(50,50,100,100, fill="red",width=10)
mincanvas.coords(i, 100,100,150,200) # change coordinates
mincanvas.itemconfig(i, fill="blue") # change color 
#mincanvas.delete(i) # remove

#For at placere widgets på canvas må der åbnes et canvas vindue
#Ønskes flere widgets i vindue kan der først placeres en frame
#Vinduet tilpasses størrelse af widget.
minwidget = tk.Label(mincanvas, text='Spam', fg='white', bg='black')
minwidget.pack()
#Bemærk at viduet refererer til den widge der skal placeres
mincanvas.create_window(180, 180, window=minwidget) 



#mincanvas.pack()

#Noget andet
minlabel=tk.Label(mitVindue,text="Hej med dig",bg="green")
minlabel.pack()
minframe=tk.Frame(mitVindue,bg="blue")
minlabel1=tk.Label(minframe,text="Hej med dig",bg="red")
minlabel1.pack()
minlabel.pack()
minframe.pack()

mitVindue.mainloop()

