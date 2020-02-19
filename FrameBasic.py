import tkinter as tk

def rammered():
    ramme=tk.Frame(mitvindue,bg='red',padx=5,pady=5)
    return ramme
def rammeblue():
    ramme=tk.Frame(mitvindue,bg='blue',padx=5,pady=5)
    return ramme
def rammegreen():
    ramme=tk.Frame(mitvindue,bg='green',padx=5,pady=5)
    return ramme


mitvindue=tk.Tk()

mitvindue.title("Vindue")
#mitvindue.geometry("400x400")

rot=rammered()
blau=rammeblue()
grun=rammegreen()

#Her refererer grid til placering i vindue da rammerne er placeret i mitvindue
rot.grid(row=0,column=0,sticky="ew")
blau.grid(row=1,column=0,sticky="ew")
grun.grid(row=2,column=0,sticky="ew")


tekstrot1=tk.Label(rot,text="Min")
tekstrot2=tk.Label(rot,text="røde",bg="pink")
tekstrot3=tk.Label(rot,text="ramme")
tekstblau1=tk.Label(blau,text="Blå")
tekstgrun1=tk.Label(grun,text="Grøn bred kolonne")

#Her referer grid til de 3 rammer rot, blua og grun da teksterne er placeret i disse rammer
tekstrot1.grid(row=0,column=0)
tekstrot2.grid(row=0,column=1,sticky="e")
tekstrot3.grid(row=0,column=2)
tekstblau1.grid(row=0,column=0,sticky="ew")
tekstgrun1.grid(row=0,column=0)

mitvindue.mainloop()

