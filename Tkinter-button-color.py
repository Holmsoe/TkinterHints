import tkinter as tk

mitVindue = tk.Tk()

def doSomething():
   print("Du trykkede på knappen")
   print("Ha ha ha ha ")

MinKnap1=tk.Button (mitVindue, text='Hej med dig')

#Background color
#===========================================================================

# colorpicker here
# https://www.w3schools.com/colors/colors_picker.asp

colortype=2

if colortype==1:
   #rgb
    mycolor1='#%02x%02x%02x' % (0, 204, 0)
    MinKnap1.config(bg=mycolor1)
elif colortype==2:
    #hexa.
    mycolor2 = '#40E0D0'
    MinKnap1.config(bg=mycolor2)
else:
    #name. See names here:
    # http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
    mycolor3 = 'red'
    MinKnap1.config(bg=mycolor3)

#textfarve
MinKnap1.config(fg='red')

#Textlayout
#============================================================================

#heigth måles i bogstavhøjder
#width måles i bogstavbredde
#wraplength er bredden hvor texten wrappes måles i pixels
#Alignment horisontal
#Teksten placeres i midten af width hvis wraplength er mindre end width
MinKnap1.config(height=3,width=40,wraplength=70, justify='right')

#Padding and border
#============================================================================
# Padding er indenfor skrivefelt og ikke ramme
# Relief er rammens design
# bd er rammens bredde i pixel
MinKnap1.config(padx=10,pady=10,relief='ridge',bd=5)

#Dynamiske funktioner
#============================================================================
# activebackground og activeoreground er farver når man trykker på knappen
MinKnap1.config(activebackground='orchid1',activeforeground='royalblue')

#Fonts
#============================================================================
#Første er font family. se her: https://en.wikipedia.org/wiki/Font_family_(HTML)
#Anden er Font size
#tredie er weight
#Bemærk at heigth og width ændrer sig med font størrelse.

MinKnap1.config(font = ('arial','20','bold','italic'))

#Command
#=============================================================================
MinKnap1.config(command = doSomething)

MinKnap1.pack()
mitVindue.mainloop()
