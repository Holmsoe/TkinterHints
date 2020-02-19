import tkinter as tk



class HovedVindue(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Mit vindue")
        self.configure(bg="green",padx=5,pady=5)
        
        self.MineWidgets()
        
    def MineWidgets(self):
        MainLabel1=tk.Label(self,text="Label1",bg="yellow")
        MainLabel2=tk.Label(self,text="Label2",bg="pink")
        
        MainLabel1.grid(row=0,column=0,sticky="ewns")
        MainLabel2.grid(row=1,column=0,sticky="ewns")
        
        MinRamme=Ramme(self)
        MinRamme.grid(row=0,column=1,rowspan=2,sticky="ewsn")
        #MinRamme.grid(self,row=0,column=0)
        
class Ramme(tk.Frame):
    def __init__(self,vindue):
        tk.Frame.__init__(self,vindue)
        self.configure(bg="red",padx=5,pady=5)
        
        self.RammeWidgets()
        
    def RammeWidgets(self):
        TekstRamme=tk.Label(self,text="Tekst i ramme")
        TekstRamme.grid(row=0,column=0,padx=1,pady=1)
        TekstRamme=tk.Label(self,text="Ugh")
        TekstRamme.grid(row=1,column=0,padx=1,pady=1,sticky="ew")

      
mitVindue=HovedVindue()
mitVindue.mainloop()

