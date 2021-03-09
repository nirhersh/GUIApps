from backend import DataBase
from tkinter import *
app = Tk()
app.title("Book Store")
app.geometry("400x400")


database = DataBase("database.db")


def get_selected_row(event):
    global row_id
    try:
        index = list_box.curselection()
        row_id = index[0] + 1
    except IndexError:
        pass


def view_command():
    list_box.delete(0, END)
    screen = str.maketrans("()'", 3*' ')
    for row in database.view():
        corrected_row = str(row).translate(screen)
        list_box.insert(END, ''.join(corrected_row))


def search_command():
    list_box.delete(0, END)
    screen = str.maketrans("()'", 3 * ' ')
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        corrected_row = str(row).translate(screen)
        list_box.insert(END, ''.join(corrected_row))


def add_command():
    try:
        last_id = database.view()[-1][0]
        new_item_id = int(last_id) + 1
        database.insert(new_item_id, title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    except IndexError:
        new_item_id = 1
        database.insert(new_item_id, title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


def update_command():
    database.update(title_text.get(), author_text.get(), year_text.get(), isbn_text.get(), row_id)
    list_box.delete(0, END)
    view_command()


def delete_command():
    database.delete(row_id)
    list_box.delete(0, END)
    view_command()


# labels
title_label = Label(app, text="Title: ", font="Times 14")
author_label = Label(app, text="Author: ", font="Times 14")
year_label = Label(app, text="Year: ", font="Times 14")
isbn_label = Label(app, text="ISBN: ", font="Times 14")

# entry boxes
title_text = StringVar()
title_entry = Entry(app, textvariable=title_text)
author_text = StringVar()
author_entry = Entry(app, textvariable=author_text)
year_text = StringVar()
year_entry = Entry(app, textvariable=year_text)
isbn_text = StringVar()
isbn_entry = Entry(app, textvariable=isbn_text)

# viewing box
list_box = Listbox(app, width=40, height=15, selectmode=EXTENDED)
scroll_bar_y = Scrollbar(app, orient='vertical')
scroll_bar_x = Scrollbar(app, orient='horizontal')
list_box.bind('<<ListboxSelect>>', get_selected_row)

# action buttons
view_button = Button(app, text="View all records", command=lambda: view_command(), width=15)
search_button = Button(app, text="Search an entry", command=lambda: search_command(), width=15)
add_button = Button(app, text="Add", command=lambda: add_command(), width=15)
update_button = Button(app, text="Update", command=lambda: update_command(), width=15)
delete_button = Button(app, text="Delete", command=lambda: delete_command(), width=15)
close_button = Button(app, text="Close", command=lambda: app.destroy(), width=15)

# the grid
title_label.grid(row=0, column=0)
title_entry.grid(row=0, column=1)
author_label.grid(row=0, column=2)
author_entry.grid(row=0, column=3)
year_label.grid(row=1, column=0)
year_entry.grid(row=1, column=1)
isbn_label.grid(row=1, column=2)
isbn_entry.grid(row=1, column=3)
view_button.grid(row=2, column=3, columnspan=2, sticky="nse", padx=20)
search_button.grid(row=3, column=3, columnspan=2, sticky="nse", padx=20)
add_button.grid(row=4, column=3, columnspan=2, sticky="nse", padx=20)
update_button.grid(row=5, column=3, columnspan=2, sticky="nse", padx=20)
delete_button.grid(row=6, column=3, columnspan=2, sticky="nse", padx=20)
close_button.grid(row=7, column=3, columnspan=2, sticky="nse", padx=20)
list_box.grid(row=2, column=0, columnspan=3, rowspan=6)
scroll_bar_y.grid(row=2, column=3, rowspan=6, sticky="nsw")
scroll_bar_x.grid(row=9, column=0, columnspan=3, sticky="sew")
list_box.configure(yscrollcommand=scroll_bar_y.set)
list_box.configure(xscrollcommand=scroll_bar_x.set)
scroll_bar_y.configure(command=list_box.yview)
scroll_bar_x.configure(command=list_box.xview)

app.mainloop()