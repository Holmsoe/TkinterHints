import tkinter as tk

vindue=tk.Tk()

vindue.geometry("200x100+200+500") #bredde x højde+x forskydning+yforskydining
vindue.title("Mit vindue")
vindue.iconbitmap("blyant.ico")

'''

pack(fill=BOTH, expand=True)

columnconfigure(1, weight=1)
columnconfigure(3, pad=7)
rowconfigure(3, weight=1)
rowconfigure(5, pad=7)
'''       
lbl = tk.Label(text="Windows")
lbl.grid(sticky='w', pady=4, padx=5)
        
#area = tk.Text()
#area.grid(row=1, column=0, columnspan=2, rowspan=4, padx=5, sticky='ewsn')
        
abtn = tk.Button(text="Activate")
abtn.grid(row=1, column=3)

cbtn = tk.Button(text="Close")
cbtn.grid(row=2, column=3, pady=4)
        
hbtn = tk.Button(text="Help")
hbtn.grid(row=5, column=0, padx=5)

obtn = tk.Button(text="OK")
obtn.grid(row=5, column=3)        
              
  
vindue.mainloop()  
    


