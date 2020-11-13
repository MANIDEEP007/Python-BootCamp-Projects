import random
import time
from tkinter import Tk,Button, DISABLED

#Create Window Object
win = Tk()

#Make Window Size Fixed
win.resizable(width=False,height=False)

#Title for Window
win.title("Match Maker")

#Variable for controlling flipping
first = True

#Variable to remember the cards
prev_x = 0
prev_y= 0

#Symbol Variables
btns = {} #Keys are Tuples
btn_symbols = {}

#Twice Symbols
symbol = [
    u"\u2702", #Scissor
    u"\u2705", #Tick Mark
    u"\u2708", #AeroPlane
    u"\u2709", #Mail
    u"\u270a", #Hand Closed
    u"\u270b", #Hand Raised
    u"\u270c", #Peace symbol
    u"\u270f", #Pencil
    u"\u2712", #Tongs
    u"\u2714", #Right Mark
    u"\u2716", #Cross
    u"\u2728", #Stars
    u"\u2702", #Scissor
    u"\u2705", #Tick Mark
    u"\u2708", #AeroPlane
    u"\u2709", #Mail
    u"\u270a", #Hand Closed
    u"\u270b", #Hand Raised
    u"\u270c", #Peace symbol
    u"\u270f", #Pencil
    u"\u2712", #Tongs
    u"\u2714", #Right Mark
    u"\u2716", #Cross
    u"\u2728", #Stars
    ]

#Shuffle Symbols for randomness
random.shuffle(symbol)

#Function to Show Symbols
def show_symbol(x,y):
    global first
    global prev_x,prev_y
    #Add Symbol to Button
    btns[x,y]['text'] = btn_symbols[x,y]
    btns[x,y].update_idletasks()
    if first:
        prev_x = x
        prev_y = y
        first = False
    #Not Clicking Same button
    elif prev_x != x or prev_y !=y:
        #Match Occured
        if btns[x,y]['text'] != btns[prev_x,prev_y]['text']:
            time.sleep(0.5)
            btns[prev_x,prev_y]['text'] = ""
            btns[x,y]['text'] = ""
        #Match Not Occured
        else:
            btns[prev_x,prev_y]['command'] = DISABLED
            btns[x,y]['command'] = DISABLED
        first=True

#Add Buttons using Nested Loops
for i in range(6):
    for j in range(4):
        button = Button(width=10,height=8,command=lambda x=i,y=j:show_symbol(x,y))
        button.grid(row=j,column=i)
        btns[i,j] = button
        btn_symbols[i,j] = symbol.pop()

win.mainloop()
