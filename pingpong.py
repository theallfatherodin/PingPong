import turtle
import winsound

wn = turtle.Screen()
wn.title("PingPong by Tapash")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_a=0
score_b=0

# Paddle A

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1, outline=3)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1, outline=1.5)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball

ball1 = turtle.Turtle()
ball1.speed(0)
ball1.shape("square")
ball1.color("red")
ball1.penup()
ball1.goto(0, 0)
ball1.dx = 0.1
ball1.dy = 0.1

ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("square")
ball2.color("green")
ball2.penup()
ball2.goto(0, 0)
ball2.dx = -0.2
ball2.dy = -0.2

ball3 = turtle.Turtle()
ball3.speed(0)
ball3.shape("square")
ball3.color("yellow")
ball3.penup()
ball3.goto(0, 0)
ball3.dx = -0.1
ball3.dy = 0.1

balls = [ball1, ball2, ball3]

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font= ("Courier", 20, "normal"))


#Function
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard Binding 
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#main game loop
while True:
    wn.update()

    for ball in balls:

       # Move the ball
       ball.setx(ball.xcor() + ball.dx)
       ball.sety(ball.ycor() + ball.dy)

       # Board checking
       if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC )


       if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1 
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC )


       if ball.xcor() > 390:
            ball.goto(0,0)
            ball.dx *= -1   
            score_a +=1
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC )
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font= ("Courier", 20, "normal"))

       if ball.xcor() < -390:
            ball.goto(0,0)
            ball.dx *= -1  
            score_b +=1
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC )
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font= ("Courier", 20, "normal"))


        # Paddle and ball collisions
       if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() +40 and ball.ycor() > paddle_b.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC )


       if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() +40 and ball.ycor() > paddle_a.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC )

    # AI Player
    closest_ball = balls[0]
    for ball in balls:
        if ball.xcor() > closest_ball.xcor():
            closest_ball = ball
    if paddle_b.ycor() < closest_ball.ycor() and abs(paddle_b.ycor() - closest_ball.ycor() < 20):
        paddle_b_up()
        
    elif paddle_b.ycor() > closest_ball.ycor() and abs(paddle_b.ycor() - closest_ball.ycor() > 20):
        paddle_b_down()
