import random
import turtle as t
from turtle import *

franklin = t.Turtle()
t.colormode(255)
franklin.shape('turtle')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

#demo
#franklin.color('red', 'yellow')
#franklin.begin_fill()
#while True:
#    franklin.forward(200)
#    franklin.left(170)
#    if abs(franklin.pos()) < 1:
#        break
#franklin.end_fill()

# random turle walk
colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'Wheat', 'SlateGray', 'SeaGreen']
directions = [0, 90, 180, 270]
franklin.pensize(14)
franklin.speed(60)
for a in range(400):
    franklin.color(random_color())
    franklin.forward(30)
    franklin.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()