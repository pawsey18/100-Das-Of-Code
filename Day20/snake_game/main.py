from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

start_pos = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for pos in start_pos:
    block = Turtle('square')
    block.penup()
    block.color('white')
    block.goto(pos)
    segments.append(block)




game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)


    for block_count in range(start=2, stop =0, step=-1):




screen.exitonclick()