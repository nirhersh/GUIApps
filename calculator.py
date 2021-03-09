from tkinter import *
import operator

calculator = Tk()
calculator.geometry('390x270')
calculator.title("Calculator")
calculator.configure(background='white')
actions_dict = {'+': operator.add, '-': operator.sub, '/': operator.truediv, '*': operator.mul}


def add_number(num):
    """ A function that addsm a number or dot to the calculation
     :param num: the object that the button gives
     :type num: int, except for dot, then str
     """
    current_entry = entry_box.get()
    current_value = value_box.get()
    current_value_list = current_value.split()
    if not current_value_list:
        entry_box.delete(0, END)
        entry_box.insert(0, current_entry + str(num))
    elif len(current_value_list) >= 2:
        entry_box.delete(0, END)
        entry_box.insert(0, current_entry + str(num))
        value_box.delete(0, END)
        value_box.insert(0, current_value + str(num))


def add_action(action):
    """ a function that adds an operator to the calculation
    :param action: an action that is used as a key in actions dict
    :type action: str
    """
    current_entry = entry_box.get()
    current_entry_list = current_entry.split(' ')
    current_value = value_box.get()
    current_value_list = current_value.split()
    if len(current_value_list) == 3:
        return
    elif len(current_entry) == 0:
        return
    elif len(current_entry_list) == 2:
        return
    elif (len(current_entry_list) == 3) and (len(current_value_list) == 0):
        return
    elif current_value_list and (len(current_value_list) - len(current_entry_list) == 2):
        return
    elif not current_value_list:
        entry_box.delete(0, END)
        entry_box.insert(0, current_entry + ' ' + action + ' ')
    else:
        entry_box.delete(0, END)
        entry_box.insert(0, current_entry + ' ' + action + ' ')
        value_box.delete(0, END)
        value_box.insert(0, current_value + ' ' + action + ' ')


def negate():
    """ a function that adds a minus sign before the result
    """
    current_value = value_box.get()
    current_value_list = current_value.split()
    if len(current_value_list) == 1:
        value_box.delete(0, END)
        value_box.insert(0, '-' + str(current_value))
    else:
        return


def clear_func():
    """ afunction that clears the value and entry boxes
    """
    entry_box.delete(0, END)
    value_box.delete(0, END)


def enter():
    """ a function that makes the calculation
    """
    current_value = value_box.get()
    current_entry = entry_box.get()
    current_entry_list = current_entry.split(' ')
    current_value_list = current_value.split()
    if not current_value_list:
        new_value = actions_dict[current_entry_list[1]](float(current_entry_list[0]), float(current_entry_list[2]))
        if str(new_value)[-1] != '0':
            value_box.delete(0, END)
            value_box.insert(0, str(new_value))
        else:
            value_box.delete(0, END)
            value_box.insert(0, str(new_value)[:-2])
    elif len(current_value_list) == 3:
        new_value = actions_dict[current_value_list[1]](float(current_value_list[0]), float(current_value_list[2]))
        if str(new_value)[-1] != '0':
            value_box.delete(0, END)
            value_box.insert(0, str(new_value))
        else:
            value_box.delete(0, END)
            value_box.insert(0, str(new_value)[:-2])

# number_buttons


button1 = Button(calculator, text='1', command=lambda: add_number(1), padx=15, pady=15)
button2 = Button(calculator, text='2', command=lambda: add_number(2), padx=15, pady=15)
button3 = Button(calculator, text='3', command=lambda: add_number(3), padx=15, pady=15)
button4 = Button(calculator, text='4', command=lambda: add_number(4), padx=15, pady=15)
button5 = Button(calculator, text='5', command=lambda: add_number(5), padx=15, pady=15)
button6 = Button(calculator, text='6', command=lambda: add_number(6), padx=15, pady=15)
button7 = Button(calculator, text='7', command=lambda: add_number(7), padx=15, pady=15)
button8 = Button(calculator, text='8', command=lambda: add_number(8), padx=15, pady=15)
button9 = Button(calculator, text='9', command=lambda: add_number(9), padx=15, pady=15)
button0 = Button(calculator, text='0', command=lambda: add_number(0), padx=15, pady=15)
dot_button = Button(calculator, text='.', command=lambda: add_number('.'), padx=17, pady=15)


# action buttons


plus_button = Button(calculator, text='+', command=lambda: add_action('+'), padx=14, pady=15, bg="green")
minus_button = Button(calculator, text='-', command=lambda: add_action('-'), padx=15, pady=15, bg="red")
division_button = Button(calculator, text='/', command=lambda: add_action('/'), padx=15, pady=15, bg="red")
multiple_button = Button(calculator, text='x', command=lambda: add_action('*'), padx=15, pady=15, bg="green")
clear_button = Button(calculator, text="clear", command=lambda: clear_func(), padx=46, pady=15)
enter_button = Button(calculator, text="enter", command=lambda: enter(), padx=46, pady=15, bg="orange")
negate_button = Button(calculator, text='(-)', command=lambda: negate(), padx=12, pady=15)

# the entry box
entry_box = Entry(calculator, width=65, borderwidth=5)
value_box = Entry(calculator, width=65, borderwidth=5)

# the grid
entry_box.grid(row=1, column=0, columnspan=5)
value_box.grid(row=2, column=0, columnspan=5)
button0.grid(row=6, column=0)
button1.grid(row=5, column=0)
button4.grid(row=4, column=0)
button7.grid(row=3, column=0)
enter_button.grid(row=5, column=3, columnspan=2)
dot_button.grid(row=6, column=1)
button2.grid(row=5, column=1)
button5.grid(row=4, column=1)
button8.grid(row=3, column=1)
clear_button.grid(row=6, column=3, columnspan=2)
negate_button.grid(row=6, column=2)
button3.grid(row=5, column=2)
button6.grid(row=4, column=2)
button9.grid(row=3, column=2)
plus_button.grid(row=4, column=3)
minus_button.grid(row=4, column=4)
multiple_button.grid(row=3, column=3)
division_button.grid(row=3, column=4)

calculator.mainloop()
