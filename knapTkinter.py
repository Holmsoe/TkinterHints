import tkinter as tk
window=tk.Tk()

#==================== Hjælperutiner ==================================
def min_knap():
    button.config(text="slut",command=ud)
    
def ud():
    print("Vi stopper nu")
    
count=0
def taelle_knap():
    global count
    count=count+1
    button.config(text=str(count))

def tekst_sub():
    mintekst=entry.get()        #her læses teksten i vinduet
    entry.insert(0,mintekst)    #her sættes teksten tilbage i vinduet

def tekst_vend():
    mintekst=entry.get()
    mintekst=mintekst[::-1]     #her vendes teksten bagfra
    entry.delete(0,tk.END)      #her slettes tekst i vindue
    entry.insert(0,mintekst)    #her indsættes den bagvendte tekst

def password_tjek():
    password="abekat"
    password_ind=passwordEntry.get()
    if password==password_ind:
        confirmLabel.config(text="I orden")
    else:
        confirmLabel.config(text="Forkert")
        
        
#=====================================================================

OK=False

while OK != True:

    print('Du har følgende mulighder:')
    print('1. Ændre knap ved tryk og stoppe')
    print('2. Tælle antal tryk og skrive på knap')
    print('3. Skrive en tekst i knapvindue og ved tryk kopiere denne tekst til vindue')
    print('4. Skrive en tekst og skrive i vinduet bagfra')
    print('5. Input og tjek password')
    print('6. Slut')

    tal =int(input('hvad vælger du? '))
    print('')

    if tal==1:
        button=tk.Button(window,text="Tryk her",command=min_knap)
        button.pack()
        window.mainloop()
        OK=True
    elif tal==2:
        button=tk.Button(window,text="tryk her ",command=taelle_knap)
        button.pack()
        window.mainloop()
        OK=True
    elif tal==3:
        entry=tk.Entry(window)
        button=tk.Button(window,text="tekstgentag",command=tekst_sub)
        entry.pack()
        button.pack()
        window.mainloop()
        OK=True
    elif tal==4:
        entry=tk.Entry(window)
        button=tk.Button(window,text="tekstvend",command=tekst_vend)
        entry.pack()
        button.pack()
        window.mainloop()
        OK=True
    elif tal==5:
        passwordLabel=tk.Label(window,text="Password: ")
        passwordEntry=tk.Entry(window,show="*")
        button=tk.Button(window,text="Enter",command=password_tjek)
        confirmLabel=tk.Label(window)
        passwordLabel.pack()
        passwordEntry.pack()
        button.pack()
        confirmLabel.pack()
        window.mainloop()
    elif tal==6:
        OK=True
    else:
        print('forkert valg')
        print('')
    


