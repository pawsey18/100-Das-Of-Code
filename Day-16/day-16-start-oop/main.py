from turtle import Turtle, Screen
# import another_module
franklin = Turtle()
# my_number = another_module.another_variable
my_screen = Screen()

franklin.shape('turtle')
franklin.color('green', 'black')
franklin.isvisible()
franklin.forward(99)
print(my_screen.canvheight)
print(my_screen.window_width())
my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])

table.align = "l"

print(table)
