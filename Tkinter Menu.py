import tkinter as tk

mitVindue = tk.Tk()

def hello():
    print ("hello!")
def goodbye():
    print ("good bye!")

def tjek():
    if varTjek.get()==0:
        print ("no tjek!")
    else:
        print ("tjek!")

counter = 0

def update():
    global counter
    counter = counter + 1
    menu.entryconfig(0, label=str(counter))


# create a toplevel menu
menubar = tk.Menu(mitVindue)
menubar.add_command(label="Hello!", command=hello)
menubar.add_command(label="Quit!", command=goodbye)

# create a pulldown menu, and add it to the menu bar
filemenu = tk.Menu(menubar, tearoff=0)  #Bemærk link til menubar
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=goodbye)

menubar.add_cascade(label="File", menu=filemenu)    #Bemærk hvordan punkterne i menu linkes op til overskrift

# create more pulldown menus
editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)

varTjek = tk.IntVar(  )
editmenu.add_checkbutton(label='MinCheckbutton', var=varTjek, command=tjek)

menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=hello)
menubar.add_cascade(label="Help", menu=helpmenu)

#You can use the postcommand callback to update (or even create) the menu every time it is displayed.
menu = tk.Menu(menubar, tearoff=0, postcommand=update)
menu.add_command(label=str(counter)) #Variabel som menupunkt
menu.add_command(label="Exit", command=goodbye)

menubar.add_cascade(label="Test", menu=menu)




# display the menu
mitVindue.config(menu=menubar)


mitVindue.mainloop()
