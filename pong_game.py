#Importing necessary libraries
import turtle
import random
import time

win=turtle.Screen()
win.title("Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0) 

#Speed
initial_speed=4
speed_up_by=0.5

#Colours
colour=["red","blue","green","yellow","pink","purple"]

#Score
score_a=0
score_b=0

#Paddle A
pad_a=turtle.Turtle() 
pad_a.speed(0) 
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(-350,0)

#Paddle B
pad_b=turtle.Turtle() 
pad_b.speed(0) 
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(350,0)

#Ball
ball=turtle.Turtle() 
ball.speed(0) 
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = initial_speed
ball.dy = -initial_speed

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup() 
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier",24,"bold"))

#Functions
def pad_a_up():
    y=pad_a.ycor()
    y+=20
    pad_a.sety(y)

def pad_a_down():
    y=pad_a.ycor()
    y-=20
    pad_a.sety(y)

def pad_b_up():
    y=pad_b.ycor()
    y+=20
    pad_b.sety(y)

def pad_b_down():
    y=pad_b.ycor()
    y-=20
    pad_b.sety(y)

#Keyboard binding
win.listen()
win.onkeypress(pad_a_up,"w")
win.onkeypress(pad_a_down,"s")
win.onkeypress(pad_b_up,"Up")
win.onkeypress(pad_b_down,"Down")


#Main game loop
while True:
    time.sleep(1/60)
    win.update() 

    #Moving the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *=-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx=initial_speed
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a,score_b), align="center", font=("Courier",24,"bold"))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx=initial_speed
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score_a,score_b), align="center", font=("Courier",24,"bold"))

    #Paddle and Ball Collision
    if(ball.xcor()>340 and ball.xcor()<350 and (ball.ycor()<pad_b.ycor()+50 and ball.ycor()>pad_b.ycor()-50)):
        ball.setx(340)
        ball.dx*=-1
        ball.dx-=speed_up_by #increase speed
        random_col=random.choice(colour) #changing colour
        ball.color(random_col)

    if(ball.xcor()<-340 and ball.xcor()>-350 and (ball.ycor()<pad_a.ycor()+50 and ball.ycor()>pad_a.ycor()-50)):
        ball.setx(-340)
        ball.dx*=-1
        ball.dx+=speed_up_by #increase speed
        random_col=random.choice(colour) #changing colour
        ball.color(random_col)




