import tkinter as tk
from tkinter import ttk

mitVindue = tk.Tk()
mitVindue.geometry("400x350+200+500") #bredde x højde+x forskydning+yforskydining
mitVindue.title("Mit vindue")
mitVindue.configure(bg="pink")
mitVindue.iconbitmap("blyant.ico")

def doSomething():
   print("Du trykkede på knappen")
   print("Ha ha ha ha ")

def skrivInput(OverleveretInput):
    print(MitInput1.get())

def mitvalg(OverleveretInput):
    print(MinListBox1.get(MinListBox1.curselection()))

def vischeckbutton():
    print(chkbut.get())

def visradiobutton():
    print(radiobut.get())
    
def viscombobox(OverleveretInput):
    print(MinComboBox.get())

def visspinbox(OverleveretInput):
    print(MinSpinBox.get())

def visskala(OverleveretInput):
    print(MinSkala.get())

def hello():
    print("hello menu")

def goodbye():
    print("goodbye menu")


MinKnap1=ttk.Button (mitVindue, text='knap1',command=doSomething)
MinKnap2=ttk.Button (mitVindue, text='knap2')
MinKnap3=ttk.Button (mitVindue, text='knap3')
MinKnap4=ttk.Button (mitVindue, text='knap4')

MitInput1=ttk.Entry(mitVindue)
MitInput2=ttk.Entry(mitVindue)
MitInput3=ttk.Entry(mitVindue)
MitInput4=ttk.Entry(mitVindue)

MinLabel1=ttk.Label(mitVindue,text="Input tekst 1")
MinLabel2=ttk.Label(mitVindue,text="Input tekst 2")
MinLabel3=ttk.Label(mitVindue,text="Input tekst 3")
MinLabel4=ttk.Label(mitVindue,text="Input tekst 4")
MinLabel5=ttk.Label(mitVindue,text="Her en checkbox")
MinLabel6=ttk.Label(mitVindue,text="Her er en combobox")
MinLabel7=ttk.Label(mitVindue,text="Her er en spinbox")
MinLabel8=ttk.Label(mitVindue,text="Her er en listbox")
MinLabel9=ttk.Label(mitVindue,text="Her er en radiobutton")
MinLabel10=ttk.Label(mitVindue,text="Her er en skala")

MinListBox1=tk.Listbox(mitVindue,height=4)
MinListBox1.insert(1, "Valg1")
MinListBox1.insert(2, "Valg2")
MinListBox1.insert(3, "Valg3")

chkbut = tk.IntVar()
MinCheckbutton1 = ttk.Checkbutton(mitVindue,text="OK?",variable=chkbut,command=vischeckbutton)

radiobut=tk.StringVar()
Radio=["nr1","nr2","nr3","nr4"]
MinLabel9.grid(row=9,column=0,sticky="w",pady=5)
for  vaerdi,radiotekst in enumerate(Radio):
   MinRadioButton=ttk.Radiobutton(mitVindue,text=radiotekst,variable=radiobut,value=vaerdi+1,command=visradiobutton)
   MinRadioButton.grid(row=10,column=vaerdi)
   
MinComboBox=ttk.Combobox(mitVindue,values = ('X', 'Y', 'Z'))
MinComboBox.current(2)

MinSpinBox=tk.Spinbox(mitVindue,values=(1,2,3,4))

MinSkala = tk.Scale(mitVindue, from_=0, to=100,orient='horizontal',command=visskala)

# Text
# Toplevel
# Scale

MitInput1.bind('<Return>',skrivInput)
MinListBox1.bind('<Return>',mitvalg)
MinComboBox.bind('<Return>',viscombobox)
MinSpinBox.bind('<Return>',visspinbox)

MinLabel1.grid(row=0,column=0,sticky='w')
MinLabel2.grid(row=1,column=0,sticky='w')
MinLabel3.grid(row=2,column=0,sticky='w')
MinLabel4.grid(row=3,column=0,sticky='w',pady=5)

MitInput1.grid(row=0,column=1)
MitInput2.grid(row=1,column=1)
MitInput3.grid(row=2,column=1)
MitInput4.grid(row=3,column=1)

MinKnap1.grid(row=0,column=2)
MinKnap2.grid(row=1,column=2)
MinKnap3.grid(row=2,column=2)
MinKnap4.grid(row=3,column=2)

MinLabel5.grid(row=4,column=0,sticky='w')
MinCheckbutton1.grid(row=4,column=1,sticky='w')

MinLabel8.grid(row=5,column=1,sticky='w')
MinListBox1.grid(row=6,column=1,sticky='n')

MinLabel6.grid(row=5,column=2,sticky='w')
MinComboBox.grid(row=6,column=2,sticky='n')

MinLabel7.grid(row=5,column=0,sticky='w',pady=5)
MinSpinBox.grid(row=6,column=0,sticky='n')

MinLabel10.grid(row=7,column=0,sticky='w',pady=5)
MinSkala.grid(row=8,column=0,sticky='w')

mitVindue.mainloop()
