#Tkinter reference
#   http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/index.html

#Widget methods
#   http://effbot.org/tkinterbook/widget.htm


import sys, os, string, time
import tkinter
tk = tkinter

class CanvasDemo (tk.Frame):
    
    def __init__ (self, master):
        self.master =master
        #self.loc =self.dragged =0
        tk.Frame.__init__ (self, master)

        self.CanvasWidth=400
        self.CanvasHeight=400

        self.RectCornerx=50
        self.RectCornery=50
        self.RectWidth=150
        self.RectHeight=75

        self.Labelx=150
        self.Labely=200  

        self.mincanvas = tk.Canvas(self, width=self.CanvasWidth, height=self.CanvasHeight)

        #Rectangle
        self.mincanvas.create_rectangle(self.RectCornerx, self.RectCornery, self.RectCornerx+self.RectWidth, self.RectCornery+self.RectHeight,fill="khaki3",outline="blue",tags="mitrektangel")
            
        #widget paa canvas
        self.minLabelPaaCanvas = tk.Label(self.mincanvas, name="minlabel",text='Spam', fg='white', bg='black')
        self.LabelWindow=self.mincanvas.create_window(self.Labelx, self.Labely, window=self.minLabelPaaCanvas,tags="ugh")

        self.mincanvas.pack()

        self.minLabelPaaCanvas.bind ("<ButtonPress-1>", self.minlabel)
        self.mincanvas.tag_bind ("mitrektangel", "<ButtonPress-1>", self.rektangelTryk)
        self.mincanvas.tag_bind ("mitrektangel", "<ButtonRelease-1>", self.rektangelStop)
       
                     
    def minlabel (self, event):
        event.widget.config(bg='red')
        self.mincanvas.move(self.LabelWindow, 50, 50)  
        self.mincanvas.update()

    def rektangelTryk (self, event):
        event.widget.bind ("<Motion>", self.rektangelFlyt)       

    def rektangelFlyt (self, event):
        #print ("hej",event.x,event.y,event.time,event.x_root,event.y_root)
        #print(event.widget.coords(tk.CURRENT))
        #print(event.widget.coords("mitrektangel"))
        event.widget.itemconfigure(tk.CURRENT,fill="green")
        #event.widget.coords(tk.CURRENT,100,100,250,175)
        event.widget.coords(tk.CURRENT,event.x,event.y,event.x+250,event.y+175)

    def rektangelStop (self, event):
        event.widget.unbind ("<Motion>")
        

mitvindue =tk.Tk()
mitvindue.title ("Mit testvindue")
CanvasDemo(mitvindue).pack()
mitvindue.mainloop()
