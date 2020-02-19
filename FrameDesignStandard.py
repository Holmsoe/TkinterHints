import tkinter as tk

class vindue(tk.Tk):
    def __init__(self,sidenr):    
        tk.Tk.__init__(self)
        #self er vinduet
        self.title("Mit vindue")
        self.iconbitmap("blyant.ico")
        
        #En ramme i hovedvinduet til at indeholde de andre rammer
        hovedrammefarve = "#%02x%02x%02x" % (215, 234, 162)
        self.hovedramme=tk.Frame(self)
        self.hovedramme.configure(bg=hovedrammefarve,bd=30)
        self.hovedramme.grid(row=0,column=0,sticky=tk.W)
        
        #Liste over sider.
        #Tilføjes en ny side skal den på listen
        self.sideoversigt={1:valgramme,2:udgiftinput,3:udgiftvisret,4:udgiftny,5:mindummy}        
       
        #Her vises startsiden
        aktuelside=self.sideoversigt[sidenr]
        # rammen skal bruge et vindue som argument og det er self
        minramme=aktuelside(self.hovedramme,self) #aktuelside er en Frame= en af siderne i klasser nedenfor
        minramme.grid(row=0,column=0)
        
    def visramme(self,sidenr):
        aktuelside=self.sideoversigt[sidenr]
        minramme=aktuelside(self.hovedramme,self)
        minramme.grid(row=0,column=0,sticky="ewns")
        minramme.tkraise()

class valgramme(tk.Frame):
    def __init__(self,hovedramme,hovedvindue):  
        tk.Frame.__init__(self,hovedramme)
        
        valgrammefarve="#%02x%02x%02x" % (250, 195, 100)
        tekstfarve="#%02x%02x%02x" % (159, 202, 152)
        self.configure(padx=15,pady=15,bg=valgrammefarve)
      
 
        knapquit=tk.Button(self,text="Quit",bg="pink",font="10",command=hovedvindue.destroy)
       
        overskrift=tk.Label(self, text="Udgifter",bg=tekstfarve,font="verdana 15 bold")
        knapinput=tk.Button(self,text="Input i fil",bg="pink",font="10",command=lambda: hovedvindue.visramme(2))
        knapnyfil=tk.Button(self,text="Ny fil",bg="pink",font="10",command=lambda: hovedvindue.visramme(4)) 
        knapvisfil=tk.Button(self,text="Vis og ret fil",bg="pink",font="10",command=lambda: hovedvindue.visramme(3))
        
        ioverskrift=tk.Label(self, text="Indtægter",bg=tekstfarve,font="verdana 15 bold")
        iknapinput=tk.Button(self,text="Input i fil",bg="pink",font="10",command=lambda: hovedvindue.visramme(5))
        iknapnyfil=tk.Button(self,text="Ny fil",bg="pink",font="10",command=lambda: hovedvindue.visramme(5)) 
        iknapvisfil=tk.Button(self,text="Vis og ret fil",bg="pink",font="10",command=lambda: hovedvindue.visramme(5))
        
        roverskrift=tk.Label(self, text="Regnskab",bg=tekstfarve,font="verdana 15 bold")
        rlavregn=tk.Button(self,text="Lav regnskab",bg="pink",font="10",command=lambda: hovedvindue.visramme(5))
        rvisregn=tk.Button(self,text="Vis regnskab",bg="pink",font="10",command=lambda: hovedvindue.visramme(5)) 
        
        koverskrift=tk.Label(self, text="Kontoplan",bg=tekstfarve,font="verdana 15 bold")
        kvaelgkonto=tk.Button(self,text="Vælg kontoplan",bg="pink",font="10",command=lambda: hovedvindue.visramme(5))
        klavkonto=tk.Button(self,text="Lav kontoplan",bg="pink",font="10",command=lambda: hovedvindue.visramme(5))
        
        knapquit.grid(row=0,column=0,pady=30)

        overskrift.grid(row=1,column=0,padx=50,sticky="we")
        knapinput.grid(row=2,column=1,pady=(30,5),sticky="we")
        knapnyfil.grid(row=3,column=1,pady=5,sticky="we")
        knapvisfil.grid(row=4,column=1,pady=5,sticky="we")
        
        ioverskrift.grid(row=1,column=2,padx=50,sticky="ewsn")
        iknapinput.grid(row=2,column=3,pady=(30,5),sticky="ewsn")
        iknapnyfil.grid(row=3,column=3,pady=5,sticky="ewsn")
        iknapvisfil.grid(row=4,column=3,pady=5,sticky="ewsn")
        
        roverskrift.grid(row=5,column=0,padx=50,pady=(30,5),sticky="ew")
        rlavregn.grid(row=6,column=1,pady=(30,5),sticky="ew")
        rvisregn.grid(row=7,column=1,pady=5,sticky="ew")
        
        koverskrift.grid(row=5,column=2,padx=50,pady=(30,5),sticky="ewsn")
        kvaelgkonto.grid(row=6,column=3,pady=(30,5),sticky="ewsn")
        klavkonto.grid(row=7,column=3,pady=5,sticky="ewsn")


class udgiftinput(tk.Frame):
    def __init__(self,hovedramme,hovedvindue):  
        tk.Frame.__init__(self,hovedramme)
        
        rammefarve = "#%02x%02x%02x" % (190, 219, 186)
        self.configure(bg=rammefarve,padx=50,pady=50)
          
        minlabel = tk.Label(self, text="Udgiftinput")
        minknap=tk.Button(self,text="Back",command=lambda: hovedvindue.visramme(1))
        
        minlabel.grid(row=0,column=0,padx=5,pady=5)
        minknap.grid(row=0,column=1,padx=5,pady=5)
        
class udgiftvisret(tk.Frame):
    def __init__(self,hovedramme,hovedvindue):  
        tk.Frame.__init__(self,hovedramme)

        rammefarve = "#%02x%02x%02x" % (190, 219, 186)
        self.configure(bg=rammefarve,padx=50,pady=50)
            
        minlabel = tk.Label(self, text="Udgift vis ret ")
        minknap=tk.Button(self,text="Back",command=lambda: hovedvindue.visramme(1))
        
        minlabel.grid(row=0,column=0,padx=5,pady=5)
        minknap.grid(row=0,column=1,padx=5,pady=5)


class udgiftny(tk.Frame):
    def __init__(self,hovedramme,hovedvindue):  
        tk.Frame.__init__(self,hovedramme)

        rammefarve = "#%02x%02x%02x" % (190, 219, 186)
        self.configure(bg=rammefarve,padx=50,pady=50)
            
        minlabel = tk.Label(self, text="Udgift ny")
        minknap=tk.Button(self,text="Back",command=lambda: hovedvindue.visramme(1))

        minlabel.grid(row=0,column=0,padx=5,pady=5)
        minknap.grid(row=0,column=1,padx=5,pady=5)

class mindummy(tk.Frame):
    def __init__(self,hovedramme,hovedvindue):  
        tk.Frame.__init__(self,hovedramme)

        rammefarve = "#%02x%02x%02x" % (190, 219, 186)
        self.configure(bg=rammefarve,padx=50,pady=50)
            
        minlabel = tk.Label(self, text="Dummy")
        minknap=tk.Button(self,text="Back",command=lambda: hovedvindue.visramme(1))

        minlabel.grid(row=0,column=0,padx=5,pady=5)
        minknap.grid(row=0,column=1,padx=5,pady=5)       

#Vinduet styres af nr i kaldet
#Viduerne er gemt i "sideoversigt"  
#Paa denne måde kan vi vælge et vindue fra hovedprogram
mitvindue=vindue(1) #Nummer på startside


mitvindue.mainloop()

