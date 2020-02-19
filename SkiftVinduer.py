import tkinter as tk

class vindue(tk.Tk):
    def __init__(self,sidenr):    
        tk.Tk.__init__(self)
        #self er vinduet
        self.title("Mit vindue")
        self.iconbitmap("blyant.ico")
        
        #En ramme i hovedviduet til at indeholde de andre rammer
        self.hovedramme=tk.Frame(self)
        self.hovedramme.configure(padx=5,pady=5,bg="blue")
        self.hovedramme.pack()
        
        #Liste over sider.
        #Tilføjes en ny side skal den på listen
        self.sideoversigt={1:ramme1,2:ramme2,3:ramme3}        
       
        #Her vises startsiden
        #Bemærk at aktuelside er en Frame da det er argumentet i sideoversigten som er Frames
        aktuelside=self.sideoversigt[sidenr]
        # rammen skal bruge et vindue som argument og det er self
        minramme=aktuelside(self.hovedramme,self) #aktuelside er en Frame= en af siderne i klasser nedenfor
        minramme.grid(row=0,column=0,sticky="ewns")
        
    def visramme(self,sidenr):
        aktuelside=self.sideoversigt[sidenr]
        minramme=aktuelside(self.hovedramme,self)   #aktuelside er en Frame
        minramme.grid(row=0,column=0,sticky="ewns")
        minramme.tkraise()
        
class ramme1(tk.Frame):
    def __init__(self,hovedramme,hovedvindue):  
        tk.Frame.__init__(self,hovedramme)
        #self er rammen       
          
        minlabel = tk.Label(self, text="Ramme1")
        minknap=tk.Button(self,text="Til 2",command=lambda: hovedvindue.visramme(2))
        
        minlabel.grid(row=0,column=0,padx=5,pady=5)
        minknap.grid(row=0,column=1,padx=5,pady=5)
        
class ramme2(tk.Frame):
    def __init__(self,hovedramme,hovedvindue):  
        tk.Frame.__init__(self,hovedramme)
        #self er rammen
            
        minlabel = tk.Label(self, text="Ramme2")
        minknap=tk.Button(self,text="Til 1",command=lambda: hovedvindue.visramme(1))
        
        minlabel.grid(row=0,column=0,padx=5,pady=5)
        minknap.grid(row=0,column=1,padx=5,pady=5)


class ramme3(tk.Frame):
    def __init__(self,hovedramme,hovedvindue):  
        tk.Frame.__init__(self,hovedramme)
        #self er rammen
            
        minlabel = tk.Label(self, text="Ramme3")
        minknap=tk.Button(self,text="Til 1",command=lambda: hovedvindue.visramme(1))

        minlabel.grid(row=0,column=0,padx=5,pady=5)
        minknap.grid(row=0,column=1,padx=5,pady=5)

        inputlabel = tk.Label(self, text="Til vindue ?")
        inputlabel.grid(row=1,column=0,padx=5,pady=5)
        

#Vinduet styres af nr i kaldet
#Viduerne er gemt i "sideoversigt"  
#Paa denne måde kan vi vælge et vindue fra hovedprogram
mitvindue=vindue(3) #Nummer på startside


mitvindue.mainloop()

