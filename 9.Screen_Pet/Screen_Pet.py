from tkinter import Tk, HIDDEN,NORMAL, Canvas
import tkinter as tk

#Function to Toggle Eyes
def toggle_eyes():
    #Get Attribute of Canvas Object
    cur_color = can_obj.itemcget(left_eye,'fill')
    new_color = can_obj.body_color if cur_color == "white" else "white"
    cur_state = can_obj.itemcget(left_pup,'state')
    new_state = NORMAL if cur_state == HIDDEN else HIDDEN
    #Set Config of Canvas Object
    can_obj.itemconfigure(left_pup,state=new_state)
    can_obj.itemconfigure(left_eye,fill=new_color)
    can_obj.itemconfigure(right_eye,fill=new_color)
    can_obj.itemconfigure(right_pup,state=new_state)

#Toggle Puples
def toggle_pup():
    if not can_obj.crossed_eyes:
        can_obj.move(left_pup, 10,-5)
        can_obj.move(right_pup, -10,-5)
        can_obj.crossed_eyes = True
    else:
        can_obj.move(left_pup, -10,5)
        can_obj.move(right_pup, 10,5)
        can_obj.crossed_eyes = False

#Open Tongue
def toggle_tongue():
    if not can_obj.tongue_out:
        can_obj.itemconfigure(tongue_tip,state=NORMAL)
        can_obj.itemconfigure(tongue_main,state=NORMAL)
        can_obj.tongue_out = True
    else:
        can_obj.itemconfigure(tongue_tip,state=HIDDEN)
        can_obj.itemconfigure(tongue_main,state=HIDDEN)
        can_obj.tongue_out = False

#Movement of Pupils and Tongue
def cheeky(event):
    toggle_tongue()
    toggle_pup()
    hide_happy(event)
    win.after(1000,toggle_tongue)
    win.after(1000,toggle_pup)
    

#Show Happy Face
def show_happyface(event):
    if (20 <= event.x and event.x < 250) and (20 <= event.y and event.y < 350):
        can_obj.itemconfigure(left_cheek,state=NORMAL)
        can_obj.itemconfigure(right_cheek,state=NORMAL)
        can_obj.itemconfigure(happy_mouth,state=NORMAL)
        can_obj.itemconfigure(nor_mouth,state=HIDDEN)
        can_obj.itemconfigure(sad_mouth,state=HIDDEN)
        can_obj.happy_level = 10

#Normal Face
def hide_happy(event):
    can_obj.itemconfigure(left_cheek,state=HIDDEN)
    can_obj.itemconfigure(right_cheek,state=HIDDEN)
    can_obj.itemconfigure(happy_mouth,state=HIDDEN)
    can_obj.itemconfigure(nor_mouth,state=NORMAL)
    can_obj.itemconfigure(sad_mouth,state=HIDDEN)

#Sad Face
def sad_face():
    if can_obj.happy_level == 0:
        can_obj.itemconfigure(happy_mouth,state=HIDDEN)
        can_obj.itemconfigure(nor_mouth,state=HIDDEN)
        can_obj.itemconfigure(sad_mouth,state=NORMAL)
    else:
        can_obj.happy_level -= 1
    win.after(500,sad_face)
    
#Blink Eyes
def blink():
    toggle_eyes()
    #Call Function after every period of particular period
    win.after(250,toggle_eyes)
    win.after(3000,blink)

win = Tk()
win.title("Screen Pet")

#Canvas Object
can_obj = Canvas(win,width=400,height=400)
can_obj.configure(
    bg="dark blue",
    highlightthickness=0 #Remove Border
    )

#Color of the body of Screen Pet
can_obj.body_color = "SkyBlue1"

#Create Body
body = can_obj.create_oval(
    35,30, # X0,Y0
    365,350, #X1,Y1
    outline=can_obj.body_color,
    fill=can_obj.body_color
    )

#Create Ears
left_ear = can_obj.create_polygon(
    75,80,
    80,7,
    165,70,
    outline=can_obj.body_color,
    fill=can_obj.body_color
    )
right_ear = can_obj.create_polygon(
    255,45,
    325,10,
    320,90,
    outline=can_obj.body_color,
    fill=can_obj.body_color
    )

#Create Eyes
left_eye = can_obj.create_oval(
    130,110,
    160,170,
    outline="black",
    fill="white"
    )
left_pup = can_obj.create_oval(
    140,145,
    150,155,
    outline="black",
    fill="black"
    )
right_eye = can_obj.create_oval(
    230,110,
    260,170,
    outline="black",
    fill="white"
    )
right_pup = can_obj.create_oval(
    240,145,
    250,155,
    outline="black",
    fill="black"
    )

#Create Foots
left_foot = can_obj.create_oval(
    65,320,# X0,Y0
    145,360,# X1,Y1
    outline=can_obj.body_color,
    fill=can_obj.body_color
    )
right_foot = can_obj.create_oval(
    250,320,# X0,Y0
    330,360,# X1,Y1
    outline=can_obj.body_color,
    fill=can_obj.body_color
    )
#Normal Mouth
nor_mouth = can_obj.create_line(
    170,250,
    200,272,
    230,250,
    width=2,
    state=NORMAL,
    smooth=1 #Smooth Curved Line
    )

#Happy Mouth
happy_mouth = can_obj.create_line(
    170,250,
    200,282,
    230,250,
    width=2,
    state=HIDDEN,
    smooth=1 #Smooth Curved Line
    )

#Sad Mouth
sad_mouth = can_obj.create_line(
    170,250,
    200,232,
    230,250,
    width=2,
    state=HIDDEN,
    smooth=1 #Smooth Curved Line
    )

#Tongue
tongue_main = can_obj.create_rectangle(
    170,250,
    230,290,
    outline="red",
    fill="red",
    state=HIDDEN,
    )
tongue_tip = can_obj.create_oval(
    170,285,
    230,300,
    outline="red",
    fill="red",
    state=HIDDEN,
    )

#Cheek
left_cheek = can_obj.create_oval(
    70,180,
    120,230,
    outline="pink",
    fill="pink",
    state=HIDDEN,
    )

right_cheek = can_obj.create_oval(
    280,180,
    330,230,
    outline="pink",
    fill="pink",
    state=HIDDEN,
    )
can_obj.pack()

#Define Events & Actions
can_obj.bind('<Motion>',show_happyface)
can_obj.bind('<Leave>',hide_happy)
can_obj.bind('<Double-1>',cheeky)

can_obj.crossed_eyes = False
can_obj.tongue_out = False
can_obj.happy_level = 10

win.after(1000,blink)
win.after(5000,sad_face)


win.mainloop()
