import turtle as t
player_A_Score=0
player_B_Score=0

window=t.Screen()
window.title("Pong Game")
window.bgcolor("green")
window.setup(width=800,height=600)
window.tracer(0)                            #To set Screen Speed

#Creating left paddle
leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)

#Creating right paddle
rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)

#creating ball

ball=t.Turtle()
ball.speed(0.5)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballxdirection=0.2
ballydirection=0.2

#creating pen for scorecard update

pen=t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score",align="center",font=('Arial',24,'normal'))

#moving the leftpaddle

def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)

def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-90
    leftpaddle.sety(y)

#moving the right paddle

def rightpaddleup():
    y=rightpaddle.ycor()
    y=y+90
    rightpaddle.sety(y)

def rightpaddledown():
    y=rightpaddle.ycor()
    y=y-90
    rightpaddle.sety(y)

# Assign keys to play

window.listen()
window.onkeypress(leftpaddleup,"w")   
window.onkeypress(leftpaddledown,"s")   
window.onkeypress(rightpaddleup,"Up")   
window.onkeypress(rightpaddledown,"Down")   

while True:
    
    window.update()

    #moving the ball
    ball.setx(ball.xcor()+ballxdirection)                           #cor means corner
    ball.sety(ball.ycor()+ballydirection)

    #settingup border
    if ball.ycor()>290:              # For Right Top Paddle Border
        ball.sety(290)
        ballydirection=ballydirection*-1           
    
    if ball.ycor()<-290:              # For left Top Paddle Border
        ball.sety(-290)
        ballydirection=ballydirection*-1           
    
    if ball.xcor()>390:
        ball.goto(0,0)
        ballxdirection=ballxdirection
        player_A_Score=player_A_Score+1
        pen.clear()
        pen.write("player A:{}  player B:{}".format(player_A_Score,player_B_Score),align="center",font=('Arial',24,"normal"))
    
    if ball.xcor()<-390:
        ball.goto(0,0)
        ballxdirection=ballxdirection*-1
        player_B_Score=player_B_Score+1
        pen.clear()
        pen.write("player A:{}  player B:{}".format(player_A_Score,player_B_Score),align="center",font=('Arial',24,"normal"))

    
    # Handling The Collisions

    if (ball.xcor()>340) and (ball.xcor()<350) and (ball.ycor()<rightpaddle.ycor()+40 and ball.ycor()>rightpaddle.ycor()-40):
        ball.setx(340)
        ballxdirection=ballxdirection*-1 #To Inverse the direction Of ball after collision
    
    if (ball.xcor()>-340) and (ball.xcor()<-350) and (ball.ycor()<leftpaddle.ycor()+40 and ball.ycor()>leftpaddle.ycor()-40):
        ball.setx(-340)
        ballxdirection=ballxdirection*-1 #To Inverse the direction Of ball after collision