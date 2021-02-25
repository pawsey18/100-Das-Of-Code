import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()

guessed_states = []

while len(guessed_states) < 50:

    state_answer = screen.textinput(title=f'{len(guessed_states)}/50', prompt="What's another state?").title()
    score = turtle.Turtle()
    if state_answer == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
                new_data = pandas.DataFrame(missing_states)
                new_data.to_csv('states_to_learn.csv')
        break
    if state_answer in all_states:
        guessed_states.append(state_answer)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == state_answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_answer)

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
