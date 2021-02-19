from turtle import Turtle, Screen
import random

# def counter_clockwise():
#     tim.lt(10)
#
#
# def forward():
#     tim.backward(10)
#
#
# def backward():
#     tim.forward(10)
#
#
# def clockwise():
#     tim.rt(10)
#
#
# def clear():
#     screen.reset()
#
#
# screen.listen()
#
# screen.onkey(counter_clockwise, "a")
# screen.onkey(forward, "w")
# screen.onkey(backward, "s")
# screen.onkey(clockwise, "d")
# screen.onkey(clear, "c")

start_race = False


screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput("Turtle Race - Place bet", 'What turtle will win? Enter color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

for index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])
    turtles.append(new_turtle)

if user_bet:
    start_race = True

while start_race:
    for turtle in turtles:
        if turtle.xcor() > 230:
            start_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You won! the {winning_color} is the winning turtle')
            else:
                print(f'You lost the {winning_color} is the winning turtle')

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
