# Her er god forklaring p� tkinter strukturer
#https://stackoverflow.com/questions/17466561/best-way-to-structure-a-tkinter-application

import tkinter as ttk

class MainApplication:
      
    def __init__(self, vindue):             #Her initialiseres child class
        self.vindue = vindue
        self.frame = ttk.Frame(self.vindue)
        
        farve="#%02x%02x%02x" % (101,135,120)
        farve1="#%02x%02x%02x" % (135,101,120)
        
        self.vindue.config(bg=farve)
        
        self.SkriveKnap=ttk.Button(self.vindue,text="Besked",command=self.SkrivBesked,bg="grey")                
        self.NulKnap=ttk.Button(self.vindue,text="Nulstil",command=self.Nulstil,bg="grey")
        self.UdKnap=ttk.Button(self.vindue,text="Ud",command=self.UdBesked,bg="grey")
        
        self.MinLabelInput=ttk.Label(self.vindue,text="Skriv noget her",bg=farve)
        self.MinLabelList=ttk.Label(self.vindue,text="Her er en listbox",bg=farve)
        self.MinLabelSpin=ttk.Label(self.vindue,text="Her er en spin",bg=farve)
        self.MinLabelSkala=ttk.Label(self.vindue,text="Her er en skala",bg=farve)
        self.MinLabelCheck=ttk.Label(self.vindue,text="Her er en check ",bg=farve)
       
        self.inputvar=ttk.StringVar()
        self.MitInput=ttk.Entry(self.vindue,textvariable=self.inputvar,bg=farve1)
        
        ListBoxOptions=["Mit valg 1","Mit valg 2","Mit valg 3"]
        self.MinListBox=ttk.Listbox(self.vindue,activestyle="none",bg=farve1)
        for nr, tekst in enumerate(ListBoxOptions):
            self.MinListBox.insert(nr, tekst)
        self.MinListBox.selection_set(first=0)
                        
        self.spinvar=ttk.StringVar()
        self.MinSpinBox=ttk.Spinbox(self.vindue,values=(1,2,3,4),textvariable=self.spinvar,bg=farve1)

        self.skalavar = ttk.IntVar()
        self.MinSkala = ttk.Scale(self.vindue, from_=0, to=100,orient='horizontal',variable=self.skalavar,bg=farve1)
        
        self.chkvar = ttk.IntVar()
        self.MinCheckbutton = ttk.Checkbutton(self.vindue,text="OK?",variable=self.chkvar,bg=farve1)
        
        self.SkriveKnap.grid(row=0)
        self.NulKnap.grid(row=0,column=1,sticky="W")
        self.UdKnap.grid(row=0,column=1,sticky="E")
        self.MinLabelInput.grid(row=1,sticky="W")
        self.MitInput.grid(row=1,column=1,sticky="W")
        self.MinLabelList.grid(row=2,sticky="W")
        self.MinListBox.grid(row=2,column=1,sticky="W")
        self.MinLabelSpin.grid(row=3,sticky="W")
        self.MinSpinBox.grid(row=3,column=1,sticky="W")
        self.MinLabelSkala.grid(row=4,sticky="W")
        self.MinSkala.grid(row=4,column=1,sticky="W")
        self.MinLabelCheck.grid(row=5,sticky="W")
        self.MinCheckbutton.grid(row=5,column=1)
       
                
    def SkrivBesked(self):
        print(self.inputvar.get())
        print(self.MinListBox.get(self.MinListBox.curselection()))
        print(self.spinvar.get())
        print(self.skalavar.get())
        print(self.chkvar.get())

             
    def UdBesked(self):
        print("Tryk på det røde kryds")

    def Nulstil(self):
        self.MinListBox.selection_clear(0,self.MinListBox.size())
        self.MinListBox.selection_set(first=0)
        self.chkvar.set(0)
        self.spinvar.set("1")
        self.skalavar.set(0)
        self.inputvar.set("")
        

if __name__ == "__main__":
    MitVindue = ttk.Tk()
    a=MainApplication(MitVindue)
    MitVindue.mainloop()
