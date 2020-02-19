import tkinter as tk

class HovedVindue(tk.Frame):         # tk:Frame er en parent class
    def __init__(self,vindue):      #Her initialiseres child class
        tk.Frame.__init__(self)     #Her initialiseres Parent class
        b=TekstFelt()        #Her laves instance af text
        b.pack()   

class TekstFelt(tk.Text):           #Her oprettes en child til tk.Text
    def __init__(self):             #Her initialiseres child
        tk.Text.__init__(self)      #Her initialiseres parent
    

MitVindue=tk.Tk()
MitVindue.geometry('400x400')
a=HovedVindue(MitVindue).pack(expand=True)
MitVindue.mainloop()
