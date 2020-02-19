import tkinter as tk
mitVindue = tk.Tk()

# For værdier of layout se forklaring i button fil
MinLabel=tk.Label(mitVindue,text="Min label tekst",height=7,width=50)
MinLabel.config(bg="CadetBlue3",fg="red",font=('helvetica','10','bold'))
MinLabel.config(padx=10,pady=10,justify='right',wraplength=50)

#Anchor er teksten placering. Standard er center. Øvrige er verdenshjørner.
#NW,N, NE, W, CENTER,E,SW,S,SE

MinLabel.config(anchor='ne')

#Cursor option
# Se http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/cursors.html

MinLabel.config(cursor='plus')

MinLabel.pack()
mitVindue.mainloop()
