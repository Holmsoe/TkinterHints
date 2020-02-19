import tkinter as tk

window=tk.Tk()

def OpdaterSlider(slidervalg):
    red=red_slider.get()
    green=green_slider.get()
    blue=blue_slider.get()
    
    farve="#%02x%02x%02x" % (red,green,blue)
    canvas.config(bg=farve)
   
red_slider=tk.Scale(window,from_=0, to=255,command= OpdaterSlider)
green_slider=tk.Scale(window,from_=0, to=255,command= OpdaterSlider)
blue_slider=tk.Scale(window,from_=0, to=255,command= OpdaterSlider)

canvas=tk.Canvas(window,height=300,width=300)

red_slider.grid(row=1,column=1)
green_slider.grid(row=1,column=2)
blue_slider.grid(row=1,column=3)

canvas.grid(row=2,column=1,columnspan=3)   

tk.mainloop()

