#turtle graphics game
import turtle
import math
import random

#set up turtle screen
wn=turtle.Screen()
wn.bgcolor("lightgreen")

#Draw border
mypen=turtle.Turtle()
mypen.penup()
mypen.setposition(-240,-240)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(480)
    mypen.left(90)
    
#Create a player turtle
player=turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)

#create a score variable
score=0

#create multiple goals
maxgoals=10
goals=[]
for count in range(maxgoals):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-240,240),random.randint(-240,240))

speed=1

#define functions
def turnleft():
    player.left(30)
def turnright():
    player.right(30)
def increasespeed():
    global speed
    speed+=1
def isCollision(t1,t2):
    d=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if d<20:
        return True
    else:
        return False
#change direction of turtle using keyboard

turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright,"Right")
turtle.onkey(increasespeed,"Up")



#Move the turtle
while True:
    player.forward(speed)
    #Boundary checking
    if player.xcor()>230 or player.xcor()<-230 or player.ycor()>230 or player.ycor()<-230:
        player.right(180)
    
    #move the goal
    for count in range(maxgoals):
        goals[count].forward(3)

    #Boundary checking for goal
        if goals[count].xcor()>230 or goals[count].xcor()<-230 or goals[count].ycor()>230 or goals[count].ycor()<-230:
            goals[count].right(180)
            
        #collision checking
        if isCollision(player,goals[count]):
            goals[count].setposition(random.randint(-240,240),random.randint(-240,240))
            goals[count].right(random.randint(0,360))
            score+=1
            #draw the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(230,255)
            scorestring="Score= %s" %score
            mypen.write(scorestring, False, align="left", font=("Arial",14,"normal"))
        

delay=raw_input("enter")

