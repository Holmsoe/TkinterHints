import tkinter as tk
mitVindue = tk.Tk()

def skrivInput(OverleveretInput):
    print(MitInput.get())

MitInput=tk.Entry(mitVindue,bg='PaleTurquoise2',bd='10')
MitInput.config(fg='coral')

#Events to widgets
#se https://www.python-course.eu/tkinter_events_binds.php
# Her ses en liste over events
# syntax    widget.bind(event, handler) 
MitInput.bind('<Return>',skrivInput)
#samme effekt kan opnås med en ekstra knap og connected command

MitInput.pack()
mitVindue.mainloop()

