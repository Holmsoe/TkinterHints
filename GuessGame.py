import tkinter as tk
import random
window=tk.Tk()

Max_tal=10
Score=0
Runder=0

def Knap_klik():
    global Score
    global Runder
    try:
        gaet=int(gaet_Box.get())
        if 1 <= gaet <= 10:
            random_tal=random.randrange(1,Max_tal+1)
            resultat=random_tal
            if gaet==random_tal:
                Score=Score+1
            Runder=Runder+1
        else:
            resultat="Tallet ikke inden for interval"               
    except:
        resultat="Du har ikke skrevet et tal din idiot"

    ResultatLabel.config(text=resultat)
    scoreLabel.config(text=str(Score) + "/" + str(Runder))
    gaet_Box.delete(0,tk.END)    

GaetLabel = tk.Label(window, text="Tast et tal mellem 1 og "+str(Max_tal))
gaet_Box= tk.Entry(window)
ResultatLabel=tk.Label(window)
scoreLabel=tk.Label(window)
knap=tk.Button(window,text="Gæt et tal",command=Knap_klik)

GaetLabel.pack()
gaet_Box.pack()
ResultatLabel.pack()
scoreLabel.pack()
knap.pack()
window.mainloop()

