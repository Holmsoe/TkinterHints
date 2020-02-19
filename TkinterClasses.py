from tkinter import *

class MineKnapper:
    def __init__(self,vindue):
        MinRamme=Frame(vindue)
        MinRamme.pack()

        self.SkriveKnap=Button(MinRamme,text="Besked",command=self.SkrivBesked)
        self.SkriveKnap.pack(side="left")

        self.UdKnap=Button(MinRamme,text="Ud",command=MinRamme.quit())
        self.UdKnap.pack(side="left")

    def SkrivBesked(self):
        print("hejsa din tumpe")

MitVindue=Tk()

b=MineKnapper(MitVindue)

MitVindue.mainloop()
