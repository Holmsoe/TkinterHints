from tkinter import *

root = Tk()
root.title('Model Definition')
root.geometry('{}x{}'.format(460, 350))

# create all of the main containers
top_frame = Frame(root, bg='cyan', width=450, height=50, pady=10)
center = Frame(root, bg='gray', width=50, height=40, padx=3, pady=3)
btm_frame = Frame(root, bg='red', width=450, height=45, pady=3)
btm_frame2 = Frame(root, bg='pink', width=450, height=60, pady=3)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

top_frame.grid(row=0, sticky="ew")
center.grid(row=1, sticky="nsew")
btm_frame.grid(row=3, sticky="ew")
btm_frame2.grid(row=4, sticky="ew")

# create the widgets for the top frame
model_label = Label(top_frame, text='Model Dimensions',bg='pink')
width_label = Label(top_frame, text='Width:',bg='gray')
length_label = Label(top_frame, text='Length:',bg='gray')
entry_W = Entry(top_frame, background="pink")
entry_L = Entry(top_frame, background="orange")

# layout the widgets in the top frame
model_label.grid(row=0, columnspan=4,sticky="ew")
width_label.grid(row=1, column=0)
length_label.grid(row=1, column=2)
entry_W.grid(row=1, column=1)
entry_L.grid(row=1, column=3)

# create the center widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)

ctr_left = Frame(center, bg='blue', width=100, height=190)
ctr_mid = Frame(center, bg='yellow', width=250, height=190, padx=3, pady=3)
ctr_right = Frame(center, bg='green', width=100, height=190, padx=3, pady=3)

ctr_left.grid(row=0, column=0, sticky="ns")
ctr_mid.grid(row=0, column=1, sticky="nsew")
ctr_right.grid(row=0, column=2, sticky="ns")

root.mainloop()

'''
As a general rule of thumb you should never call grid, 
pack or place as part of the same statement that creates the widget. 
Partially it is for this exact behavior that you're experiencing, 
but also because I think it makes your code harder to write and harder to maintain over time.
Widget creation and widget layout are two different things. In my experience, 
layout problems are considerably easier to debug when you group your layout commands together.
Also, you should be consistent when using grid and always put the options in the same order 
so you can more easily visualize the layout. And finally, 
when using grid you should get in the habit of always specifying the sticky option, 
and always give one row and one column in each containing frame a non-zero weight.
'''