import turtle
import time

win = turtle.Screen()
win.title("Breakout")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
for y in range(5):
    for x in range(-350, 400, 70):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[y])
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.goto(x, 250 - y*30)
        bricks.append(brick)

# Functions
def paddle_right():
    x = paddle.xcor()
    if x < 350:
        x += 40
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    if x > -350:
        x -= 40
    paddle.setx(x)

win.listen()
win.onkeypress(paddle_right, "Right")
win.onkeypress(paddle_left, "Left")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Paddle collision
    if (ball.ycor() > -240 and ball.ycor() < -230) and (ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50):
        ball.sety(-230)
        ball.dy *= -1

    # Brick collision
    for brick in bricks:
        if (ball.distance(brick) < 27):
            ball.dy *= -1
            brick.goto(1000, 1000)
            bricks.remove(brick)
