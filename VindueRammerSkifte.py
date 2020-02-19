import tkinter as tk

class vindue(tk.Tk):
    def __init__(self,nr):    
        tk.Tk.__init__(self)
        #self er vinduet
        self.title("Mit vindue")
        self.iconbitmap("blyant.ico")
        
        sideoversigt={1:ramme,2:ramme1,3:ramme2}
        aktuelside=sideoversigt[nr]
        
        #En ramme i hovedviduet til at indeholde de andre rammer
        hovedramme=tk.Frame(self)
        hovedramme.configure(padx=5,pady=5,bg="blue")
        hovedramme.pack()
                
        # rammen skal bruge et vindue som argument og det er self
        minramme=aktuelside(hovedramme)
        minramme.grid(row=0,column=0) 
 

class ramme(tk.Frame):
    def __init__(self,hovedramme):       
        tk.Frame.__init__(self,hovedramme)
        #self er rammen
        
        self.configure(padx=5,pady=5,bg="red")
        label1=tk.Label(self,text="buh",bg="yellow")
        label2=tk.Label(self,text="ugh",bg="green")
        label3=tk.Label(self,text="bøvs                   ups",bg="pink")
        label1.grid(row=0,column=0,sticky="ew")
        label2.grid(row=0,column=1,sticky="ew")
        label3.grid(row=1,column=0,sticky="ew")
        
class ramme1(tk.Frame):
    def __init__(self,hovedramme):       
        tk.Frame.__init__(self,hovedramme)
        #self er rammen
        
        self.configure(padx=5,pady=5,bg="pink")
        label1=tk.Label(self,text="buh",bg="yellow")
        label2=tk.Label(self,text="ugh",bg="green")
        label3=tk.Label(self,text="bøvs                   ups",bg="pink")
        label1.grid(row=0,column=0,sticky="ew")
        label2.grid(row=0,column=1,sticky="ew")
        label3.grid(row=1,column=0,sticky="ew")
        
class ramme2(tk.Frame):
    def __init__(self,hovedramme):  
        tk.Frame.__init__(self,hovedramme)
        #self er rammen
        
        def sighej():
            print("hejsa")
            
        minlabel = tk.Label(self, text="Her er en side")
        minlabel.pack(padx=5,pady=5)
        minknap=tk.Button(self,text="Sig hej",command=sighej)
        minknap.pack()
     

#Vinduet styres af nr i kaldet
#Viduerne er gemt i "sideoversigt"  
#Paa denne måde kan vi vælge et vindue fra hovedprogram
mitvindue=vindue(1)


mitvindue.mainloop()

