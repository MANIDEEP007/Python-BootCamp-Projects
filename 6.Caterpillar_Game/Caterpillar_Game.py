import turtle as t
import random as rd
import time
#Set Background Color
t.bgcolor("yellow")

#Caterpillar
caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

#Leaf - Hexagon
leaf_turtle = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
'''Register Leaf'''
t.register_shape('leaf',leaf_shape)
leaf_turtle.shape('leaf')
leaf_turtle.color("green")
leaf_turtle.penup()
leaf_turtle.speed()
leaf_turtle.hideturtle()

#Text - Write Method to write text
text_turtle = t.Turtle()
'''
Write Arguments - Arg, Alignment, Font
Alignment - Left, Right, Center
'''
text_turtle.write(
    "Press Space to Start",
    align="center",
    font=("Arial",18,"bold"), #Tuple of Name,Size, Type
    )
text_turtle.hideturtle()

#Score
score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

#OutSide Window
def outside_window():
    #Define Walls
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = - t.window_height()/2
    x,y = caterpillar.pos() #Get Position of Turtle
    outside = x < left_wall or x > right_wall or y > top_wall or y < bottom_wall
    return outside

#Place Leaf
def place_leaf():
    leaf_turtle.hideturtle()
    #Set Leaf Randomly
    leaf_turtle.setx(rd.randint(-200,200))
    leaf_turtle.sety(rd.randint(-200,200))
    leaf_turtle.showturtle()

#Game Over
def game_over():
    #Change Background to Screen Backgrounds
    caterpillar.color("yellow")
    leaf_turtle.color("yellow")
    t.penup()
    t.hideturtle()
    t.write("GAME OVER!!",align="center",font=("Arial",30,"bold"))

#Display Score
def display_score(cur_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width()/2) - 50
    y = (t.window_height()/2) - 60
    score_turtle.setx(x)
    score_turtle.sety(y)
    score_turtle.write(str(cur_score),align="right",font=("Arial",40,"bold"))

#Game Logic
def start_game():
    global game_start
    if game_start:
        return
    game_start = True
    score = 0
    text_turtle.clear() #Clear Press Space to Start
    caterpillar_speed = 2
    caterpillar_length = 3
    caterpillar.shapesize(1,caterpillar_length,1) #Stretch Width, Length, Outline
    caterpillar.showturtle()
    display_score(score)
    place_leaf()
    while(True):
        caterpillar.forward(caterpillar_speed)
        #Check reached leaf or not
        if caterpillar.distance(leaf_turtle) < 20:
            place_leaf()
            caterpillar_length += 1
            caterpillar_speed += 1
            caterpillar.shapesize(1,caterpillar_length,1)
            score += 10
            display_score(score)
        if outside_window():
            game_over()
            break

def move_up():
    #Right or Left
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)

def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)

#Function & Key as arguments
game_start = False
t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_down,'Down')
t.onkey(move_right,'Right')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()

time.sleep(3)
