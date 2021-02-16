import colorgram
# # Making a list to hold our generated colors
# rgb_colors = []
#
# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 6)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
#
# print(rgb_colors)
import turtle as turtle_module
import random

turtle_module.colormode(255)
frank = turtle_module.Turtle()
frank.speed('fastest')
frank.penup()
color_list = [(2, 164, 170), (140, 45, 141), (226, 233, 233), (149, 175, 50), (244, 211, 118), (112, 80, 40), (140, 30, 19), (172, 154, 40)]

frank.setheading(225)
frank.forward(250)
frank.setheading(0)
dots = 101
frank.end_fill()
for dot_count in range(1, dots):
    frank.dot(20, random.choice(color_list))
    frank.forward(50)

    if dot_count == 100:
        frank.hideturtle()

    if dot_count % 10 == 0:
        frank.setheading(90)
        frank.forward(50)
        frank.setheading(180)
        frank.forward(500)
        frank.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()
