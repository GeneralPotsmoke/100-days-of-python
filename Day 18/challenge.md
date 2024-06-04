#### Day 18: Turtle Graphics and GUIs
**Challenge:** Create a simple drawing program using the Turtle module, where users can use keyboard inputs to control the turtle.

```python
import turtle as t

turt = t.Turtle()

def move_forwards():
    turt.forward(10)

def move_backwards():
    turt.backward(10)

def turn_left():
    turt.left(10)

def turn_right():
    turt.right(10)

screen = t.Screen()
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.exitonclick()
```


