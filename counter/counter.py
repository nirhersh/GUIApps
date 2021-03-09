from tkinter import *
from tkinter import ttk
import winsound


counter = Tk()
counter.title("Counter")
counter.geometry('500x205')
background_image = PhotoImage(file="source.gif")
background_label = Label(counter, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
choose_frame = Frame(counter, bg="black", relief=SUNKEN, borderwidth=15)
choose_frame.pack()

colon_label1 = Label(choose_frame, text=':', fg='white', font="David 20 bold", bg="black")
colon_label2 = Label(choose_frame, text=':', fg='white', font="David 20 bold", bg="black")
colon_label1.grid(row=0, column=1)
colon_label2.grid(row=0, column=3)


# hours code
hours = ttk.Combobox(choose_frame, width=5)
hours_list = []
for i in range(0, 25):
    if i < 10:
        hours_list.append(f'{i:02}')
    else:
        hours_list.append(i)
hours['values'] = hours_list
hours.grid(row=0, column=0)

# minutes code
minutes = ttk.Combobox(choose_frame, width=5)
minutes_list = []
for i in range(0, 60):
    if i < 10:
        minutes_list.append(f'{i:02}')
    else:
        minutes_list.append(i)
minutes['values'] = minutes_list
minutes.grid(row=0, column=2)

# seconds code
seconds = ttk.Combobox(choose_frame, width=5)
seconds_list = []
for i in range(0, 60):
    if i < 10:
        seconds_list.append(f'{i:02}')
    else:
        seconds_list.append(i)
seconds['values'] = seconds_list
seconds.grid(row=0, column=4)


def counting_func(num_of_seconds):
    """A function that counts the time backwards
    :param num_of_seconds: the num of seconds the user set
    :type num_of_seconds: int
    """
    m, s = divmod(num_of_seconds, 60)
    h, m = divmod(m, 60)
    ti = (str(h).zfill(2) + ':' + str(m).zfill(2) + ':' + str(s).zfill(2))
    time_label.config(text=ti)
    num_of_seconds -= 1
    time_frame.after(1000, lambda: counting_func(num_of_seconds))
    if num_of_seconds < 0:
        winsound.Beep(1500, 205)
        time_frame.destroy()


def start_counting(hour=0, mint=0, sec=0):
    """A function that is executed when the user clicks the play button
    :param hour: number of hours the user chose
    :param mint: number of minutes the user chose
    :param sec: number of seconds the user chose
    :type hour: int
    :type mint: int
    :type sec: int
    :"""
    global time_frame
    time_frame = Frame(counter, bg='black')
    global time_label
    time_label = Label(time_frame, text='', font="Times 20 bold", bg='black', fg='white')
    when_to_stop = abs(int(hour) * 60 * 60 + int(mint) * 60 + int(sec))
    time_frame.pack(pady=10)
    time_label.pack()
    counting_func(when_to_stop)


play_button_image = PhotoImage(file="25549-9-play-button-hd.png")
enter_button = Button(choose_frame, image=play_button_image, command=lambda: start_counting(hours.get(),
                                                                                            minutes.get(),
                                                                                            seconds.get()))
enter_button.grid(row=1, column=2)


counter.mainloop()
