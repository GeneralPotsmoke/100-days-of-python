import turtle as t
import random

class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.backward(20)

class Car(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(["red", "blue", "yellow", "purple", "orange"]))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(300, random.randint(-250, 250))
        self.speed = random.randint(5, 10)

    def move(self):
        self.backward(self.speed)

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

player = Player()
cars = [Car() for _ in range(20)]

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

    for car in cars:
        car.move()
        if car.distance(player) < 20:
            game_is_on = False

    if player.ycor() > 280:
        player.goto(0, -280)

screen.exitonclick()
