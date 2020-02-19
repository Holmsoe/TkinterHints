import tkinter as tk
import random
import time

mitVindue=tk.Tk()

tidStart=time.time()
ratingGem=1000

#=============================================================================
def BeregnRating(svar,tal1,tal2,ratingGem,ventetid):
    diff=ratingGem-1200
    if diff<=200:
        korrektion=-0.1*diff+20
    else:
        korrektion=0
    
    if int(svar)==int(tal1)*int(tal2):
        NyRating=ratingGem+korrektion+1
    else:
        NyRating=ratingGem-40
    return NyRating
#=============================================================================


    
#=============================================================================    
def Regne(overleveretSvar):
    global tidStart
    global tal1
    global tal2
    global ratingGem

    #Svar hentet fra inputfelt
    svar=MitInput.get()

    #Tiden for svaret hentes og starttiden sættes til ny tid
    tidInput=time.time()
    ventetid=tidInput-tidStart
    tidStart=tidInput

    #Ny rating beregnes på baggrund af saret, tidspunktet og gammel rating
    ratingGem=BeregnRating(svar,tal1,tal2,ratingGem,ventetid)

    #Ny rating udskrives
    ResultatLabel.config(text=str(ratingGem)[0:4])  #4 første tegn i string

    #Ny regnestykke beregnes og sættes i spørgefelt
    tal1=random.randrange(2,10)
    tal2=random.randrange(2,10)
    SpoergeTekst=str(tal1)+" x "+str(tal2)
    MinLabel.config(text=SpoergeTekst)

    #Svarfelt nulstilles
    MitInput.delete(0,'end')
#=============================================================================


#Her sættes felterne i vinduet
MinLabel=tk.Label(mitVindue,height=3,width=20)
MinLabel.config(bg="CadetBlue3",fg="red",font=('helvetica','30','bold'))

MitInput=tk.Entry(mitVindue,bg='PaleTurquoise2',fg='coral',justify='center',width=22)
MitInput.config(font=('helvetica','30','bold'))

RatingLabel=tk.Label(mitVindue,text="Rating",height=1,width=20)
RatingLabel.config(bg="CadetBlue3",fg="black",font=('helvetica','30','bold'))

ResultatLabel=tk.Label(mitVindue,text=str(ratingGem),height=2,width=20)
ResultatLabel.config(bg="CadetBlue3",fg="red",font=('helvetica','30','bold'))

# Når der trykkes return i svarfeltet initieres beregningen
MitInput.bind('<Return>',Regne)

#Initialisering af regnestykke
tal1=random.randrange(2,10)
tal2=random.randrange(2,10)
SpoergeTekst=str(tal1)+" x "+str(tal2)
MinLabel.config(text=SpoergeTekst)

#Her sættes vindue op
MinLabel.pack()
MitInput.pack()
RatingLabel.pack()
ResultatLabel.pack()
mitVindue.mainloop()
