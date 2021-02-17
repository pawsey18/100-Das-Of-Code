from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def counter_clockwise():
    tim.lt(10)


def forward():
    tim.backward(10)


def backward():
    tim.forward(10)


def clockwise():
    tim.rt(10)


def clear():
    screen.reset()


screen.listen()

screen.onkey(counter_clockwise, "a")
screen.onkey(forward, "w")
screen.onkey(backward, "s")
screen.onkey(clockwise, "d")
screen.onkey(clear, "c")

screen.exitonclick()
