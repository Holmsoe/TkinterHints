import tkinter as tk

#Farver
#http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter

class Hovedvindue(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        def skrivinput():
            print(inputfelt.get())
        
        hovedramme=tk.Frame(self,padx=5,pady=5,bg="antiquewhite2")
        hovedramme.grid(row=0,column=0)
        
        inputlabel=tk.Label(hovedramme,text="Input her",bg="antiquewhite2")
        inputfelt=tk.Entry(hovedramme,bg="bisque2")
        inputskriv=tk.Button(hovedramme,text="Skriv input",height="1",bg="cornsilk3",command=skrivinput)
    
        inputlabel.grid(row=0,column=0,sticky="ewsn",padx=(0,5))
        inputfelt.grid(row=0,column=1,sticky="ewsn")
        inputskriv.grid(row=1,column=0,pady=(5,0),sticky="ew",columnspan=2)
    
Mitvindue=Hovedvindue()

Mitvindue.mainloop()

