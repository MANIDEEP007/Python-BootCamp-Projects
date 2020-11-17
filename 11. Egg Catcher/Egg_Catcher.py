from tkinter import *
from tkinter import messagebox
from itertools import cycle
from random import randrange

#Create Window Object
win = Tk()
win.title("Egg Catcher")

# Create Canvas Object
can_wid = 800
can_hei = 400
#Arg - Window Object, width, Height
can_obj = Canvas(
    win,
    width=can_wid,
    height=can_hei,
    background="deep sky blue"
    )

#Create Rectangle - Ground
can_obj.create_rectangle(
    -5,can_hei-100, #Top Left
    can_wid+5,can_hei+5, #Bottom Right
    fill="sea green",
    width=0,
    )

#Create Oval - Sun
can_obj.create_oval(
    -80,-80,
    120,120,
    fill='orange',
    width=0
    )

can_obj.pack()

#Egg related Variables
egg_wid = 45
egg_hei = 55
egg_val = 10
egg_speed = 500
egg_interval = 4000 #Interval between Egg Creation
diff_fact = 0.95 #Difficult Factor

#Function to move Catcher Left
def move_left(event):
    #Get Catcher Coordinates
    x,y,x1,y1 = can_obj.coords(catcher)
    #Move Catcher
    if x > 0:
        can_obj.move(catcher,-20,0)

#Function to move Catcher Right
def move_right(event):
    #Get Catcher Coordinates
    x,y,x1,y1 = can_obj.coords(catcher)
    #Move Catcher
    if x1 < can_wid:
        can_obj.move(catcher,20,0)

#List of Eggs
eggs = []

#Function to Create Eggs
def create_eggs():
    #Get Random X Value
    x = randrange(10,740)
    y = 40 #Egg from Certain Height
    new_egg = can_obj.create_oval(
        x,y, #Start Point
        x+egg_wid,y+egg_hei, #End Point
        fill=next(color_cycle), #Egg color
        width = 0, #Disable border
        )
    #Store Eggs in List
    eggs.append(new_egg)
    win.after(egg_interval,create_eggs)

#Function to Check Catch of Egg
def check_catch():
    #Get Catcher Coordinates
    catch_x, catch_y, catch_x1,catch_y1 = can_obj.coords(catcher)
    #Check whether egg is catched or not
    for egg in eggs:
        #Get Egg Coordinates
        egg_x,egg_y,egg_x1,egg_y1 = can_obj.coords(egg)
        #Check Wh
        if  catch_x <= egg_x and egg_x1 < catch_x1 and catch_y1 - egg_y1 < 40:
            eggs.remove(egg) #Remove egg from List
            can_obj.delete(egg) #Remove Egg from Canvas
            increase_score(egg_val) #Increase Score
    win.after(100,check_catch)

#Function to Increase Score
def increase_score(points):
    global score, egg_speed, egg_interval
    score += points
    #Increase Egg Spped & Creation of eggs Speed
    egg_speed = int(egg_speed * diff_fact)
    egg_interval = int(egg_interval * diff_fact)
    #Update Score Widget
    can_obj.itemconfigure(score_text,text="Score: "+str(score))

#Function to Drop a Egg
def egg_dropped(egg):
    eggs.remove(egg) #Remove Egg
    can_obj.delete(egg)
    lose_a_life() #Call Lose a Life Function
    if lives == 0:
        messagebox.showinfo("GAME OVER!","FINAL SCORE: "+str(score)) #Title, Content
        win.destroy()

#Function to do things when lost life
def lose_a_life():
    global lives
    lives -=1 #Decrement Life
    can_obj.itemconfigure(lives_text,text="Lives: "+ str(lives)) #Update Widget

#Function to Move Eggs
def move_eggs():
    for egg in eggs:
        egg_x,egg_y,egg_x2,egg_y2 = can_obj.coords(egg) #Get Co-ordinates of egg
        can_obj.move(egg,0,10) #Move Egg
        if egg_y > can_hei: #Reached ground, Drop Egg
            egg_dropped(egg) 
    win.after(egg_speed,move_eggs)

#Catcher Related variables
cat_wid = 100
cat_hei = 100
cat_xstart = (can_wid / 2) - (cat_wid /2)
cat_ystart = can_hei - cat_hei - 20
cat_xend = cat_xstart + cat_wid
cat_yend = cat_ystart + cat_hei

#Catcher Object
catcher = can_obj.create_arc(
    cat_xstart,cat_ystart, #Start Point
    cat_xend,cat_yend, #End Point
    start = 200, #Angle
    extent = 140, #Angle
    style="arc",
    outline = "blue",
    width = 3,
    )

#Colors List cycle
color_cycle = cycle(["light blue","light pink","light yellow","light green","red","blue","black","green"])

#Score Widget
score = 0
score_text = can_obj.create_text(
    10,10, #Point
    anchor="nw", #North West
    font=("Arial",18,"bold"), #Font
    fill="dark blue", #Color of the Text
    text="Score: " + str(score), #Text to be Written
    )

#Lives Widget
lives = 3
lives_text = can_obj.create_text(
    can_wid-10,10, #Point
    anchor="ne", #North East
    font=("Arial",18,"bold"), #Font
    fill="dark blue", #Color of the Text
    text="Lives: " + str(lives), #Text to be Written
    )

#Bind Keys & Functions
can_obj.bind('<Left>',move_left)
can_obj.bind('<Right>',move_right)
can_obj.focus_set() #Make Focus to Specific controls

win.after(1000,create_eggs) #Create Eggs after 1S
win.after(1000,move_eggs) #Move eggs after 1S
win.after(1000,check_catch) #Check Catch after 1S

win.mainloop()
