# from tkinter import *
#
# window = Tk()
#
# window.title('My first GUI in Python')
# window.minsize(width=500, height=600)
#
# # labels
# lbl_output = Label(text='shut up', font=('Arial', 24, 'bold'))
# lbl_output.pack()
#
# #entry
#
# input_thing = Entry(width=10)
# input_thing.pack()
#
#
#
# # Button
#
# def button_clicked():
#     #lbl_output.config(text='wowwwwwww sonnnnnnn')
#     lbl_output.config(text=input_thing.get())
#
#
# button = Button(text='Click It', command=button_clicked)
# button.pack()
#
#
#
# # import playground
# #
# # output_multi_args = playground.add(1, 3, 5, 7)
# # print(output_multi_args)
#
#
# window.mainloop()


# Mile to KM

from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    km_result_label.config(text=f'{km}')


window = Tk('Miles to KM Converter')
window.config(padx=20, pady=20)

miles_input = Entry(width='7')
miles_input.grid(column=1, row=0)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)

is_equal_label = Label(text='is equal to')
is_equal_label.grid(column=0, row=1)

km_result_label = Label(text='0')
km_result_label.grid(column=1, row=1)

km_label = Label(text='Km')
km_label.grid(column=2, row=1)

calc_btn = Button(text='Calculate', command=miles_to_km)
calc_btn.grid(column=1, row=2)
window.title()

window.mainloop()
