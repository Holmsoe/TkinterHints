import tkinter as tk
from tkinter import ttk

mitVindue = tk.Tk()

def doSomething():
   print("Du trykkede på knappen")
   print("Ha ha ha ha ")

def skrivInput(OverleveretInput):
    print(MitInput1.get())

def mitvalg(OverleveretInput):
    print("listbox",MinListBox1.get(MinListBox1.curselection()))

def vischeckbutton():
    print("checkbutton",chkbut.get())

def visradiobutton():
    print("radiobutton",radiobut.get())
    
def viscombobox(OverleveretInput):
    print("combo",MinComboBox.get())

def visspinbox(OverleveretInput):
    print("spin",MinSpinBox.get())

def visskala(OverleveretInput):
    print("skala",MinSkala.get())

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

MinLabel1=ttk.Label(mitVindue,text="Tryk her 1")
MinLabel2=ttk.Label(mitVindue,text="Tryk her 2")
MinLabel3=ttk.Label(mitVindue,text="Tryk her 3")
MinLabel4=ttk.Label(mitVindue,text="Tryk her 4")

MinListBox1=tk.Listbox(mitVindue)
MinListBox1.insert(1, "Valg1")
MinListBox1.insert(2, "Valg2")
MinListBox1.insert(3, "Valg3")

chkbut = tk.IntVar()
MinCheckbutton1 = ttk.Checkbutton(mitVindue,text="OK?",variable=chkbut,command=vischeckbutton)

radiobut=tk.StringVar()
Radio=["nr1","nr2","nr3","nr4"]
for  vaerdi,radiotekst in enumerate(Radio):
   MinRadioButton=ttk.Radiobutton(mitVindue,text=radiotekst,variable=radiobut,value=vaerdi+1,command=visradiobutton)
   MinRadioButton.pack()
   
MinComboBox=ttk.Combobox(mitVindue,values = ('X', 'Y', 'Z'))
MinComboBox.current(2)

MinSpinBox=tk.Spinbox(mitVindue,values=(1,2,3,4))

MinSkala = tk.Scale(mitVindue, from_=0, to=100,orient='horizontal',command=visskala)


MitInput1.bind('<Return>',skrivInput)
MinListBox1.bind('<Return>',mitvalg)
MinComboBox.bind('<Return>',viscombobox)
MinSpinBox.bind('<Return>',visspinbox)


MinKnap1.pack()
MinKnap2.pack()
MinKnap3.pack()
MinKnap4.pack()

MitInput1.pack()
MitInput2.pack()
MitInput3.pack()
MitInput4.pack()

MinLabel1.pack()
MinLabel2.pack()
MinLabel3.pack()
MinLabel4.pack()

MinListBox1.pack()

MinCheckbutton1.pack()

MinComboBox.pack()

MinSpinBox.pack()

MinSkala.pack()

mitVindue.mainloop()
