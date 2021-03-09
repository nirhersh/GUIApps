from tkinter import *
import hangman as hang
from PIL import ImageTk, Image
import random


# add a menu with a restart option


# open screen
root = Tk()
root.configure(bg="white")
root.title("Hangman by Nir Herscovici")
root.geometry("450x550")
open_screen_image = ImageTk.PhotoImage(Image.open(r"images_for_hangman\open_screen_image.png"))
open_screen_label = Label(root, image=open_screen_image).grid(row=0, column=0, columnspan=3, padx=40)
open_screen_text = Label(root, text="Welcome to Hangman", font="Times 24 bold", bg="white", padx=70)
open_screen_text.grid(row=1, column=0, pady=10)

# hangman images
hangman_images_dict = {'0': r"images_for_hangman\first.png", '1': r"images_for_hangman\second.png",
                       '2': r"images_for_hangman\third.png", '3': r"images_for_hangman\fourth.png",
                       '4': r"images_for_hangman\fifth.png", '5': r"images_for_hangman\sixth.png",
                       '6': r"images_for_hangman\seventh.png", '7': r"images_for_hangman\eighth.png"}


def chosen_letter(secret_word):
    """ a function that takes the chosen word and checks if it's in the secret word
    :param secret_word: the secret word of the game
    :type secret_word: tuple
    """
    global entry_box
    global secret_word_label
    global num_of_tries
    global hangman_image
    global hangman_label
    global letters_guessed_label
    global exit_game_button
    global invalid_input_label
    global lose_or_win
    global restart_button
    global status_bar
    letter = entry_box.get()
    letter.lower()
    entry_box.delete(0, END)
    if not hang.check_valid_input(letter, old_letters_guessed):
        invalid_input_label.configure(text=hang.try_update_letter_guessed(letter, old_letters_guessed))
        invalid_input_label.grid(row=4, column=0, columnspan=3)
    else:
        invalid_input_label.grid_forget()
        letters_guessed_label.configure(text=', '.join(old_letters_guessed))
        letters_guessed_label.grid(row=5, column=1)
        if hang.is_letter_right(letter, str(secret_word)):
            secret_word_label.configure(text=hang.show_hidden_word(secret_word, old_letters_guessed))
            if hang.check_win(str(secret_word), old_letters_guessed):
                lose_or_win.configure(text="YOU WIN")
                exit_game_button.grid(row=10, column=1, columnspan=2)
                restart_button.grid(row=10, column=0, columnspan=2)
        else:
            num_of_tries += 1
            status_bar.configure(text="You have {} guesses left".format(7 - num_of_tries))
            if num_of_tries < 7:
                hangman_image = ImageTk.PhotoImage(Image.open(hangman_images_dict[str(num_of_tries)]))
                hangman_label.configure(image=hangman_image)
            elif num_of_tries == 7:
                hangman_image = ImageTk.PhotoImage(Image.open(hangman_images_dict[str(num_of_tries)]))
                hangman_label.configure(image=hangman_image)
                lose_or_win.configure(text="YOU LOSE")
                secret_word_label.configure(text=str(secret_word))
                entry_box['state'] = DISABLED
                enter_button['state'] = DISABLED
                exit_game_button.grid(row=10, column=1, columnspan=2)
                restart_button.grid(row=10, column=0, columnspan=2)


def start_game():
    """ a function that clears the home screen and starts the game """
    global hangman_images_dict
    global hangman_label
    global entry_box
    global secret_word_label
    global status_bar
    global lose_or_win
    global enter_button
    global num_of_tries
    global hangman_frame
    global entry_box_label
    global invalid_input_label
    global hangman_image
    global old_letters_guessed
    if num_of_tries > 0:
        num_of_tries = 0
        hangman_label.pack_forget()
        for w in root.winfo_children():
            w.grid_forget()
        hangman_frame.grid(row=0, column=0, columnspan=3, padx=10)
        hangman_image = ImageTk.PhotoImage(Image.open(hangman_images_dict[str(num_of_tries)]))
        hangman_label.configure(image=hangman_image)
        hangman_label.pack()
        entry_box['state'] = NORMAL
        enter_button['state'] = NORMAL
        old_letters_guessed = []
    else:
        for w in root.winfo_children():  # clears the open screen
            w.grid_forget()
        hangman_frame.grid(row=0, column=0, columnspan=3, padx=10)
        hangman_label.configure(image=hangman_image)
        hangman_label.pack()  # the first hangman image

    index_for_word = random.randint(0, 32)
    secret_word = hang.choose_word("words.txt", index_for_word)  # the secret word to guess
    secret_word_label.configure(text=hang.underscore_word(str(secret_word)))  # the label of the secret word when its
    # underscored
    secret_word_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
    print(hang.underscore_word(str(secret_word)))
    entry_box = Entry(root, bg="white")
    enter_button = Button(root, text="Enter", command=lambda: chosen_letter(secret_word))
    lose_or_win.grid(row=8, column=1)
    lose_or_win.configure(text='')
    entry_box.grid(row=2, column=1, padx=20)
    entry_box_label.grid(row=2, column=0, columnspan=2)
    enter_button.grid(row=3, column=1, pady=10)
    status_bar.grid(row=13, column=0, columnspan=3, sticky=W + E)
    status_bar.configure(text="You have {} guesses left".format(7 - num_of_tries))


# open screen buttons
start_game_button = Button(root, text="Start game", command=lambda: start_game()).grid(row=2, column=0, pady=10)
exit_game_button = Button(root, text="Exit game", command=lambda: root.destroy())
exit_game_button.grid(row=3, column=0, pady=10)

# important variables
old_letters_guessed = []
num_of_tries = 0
entry_box = Entry(root)
hangman_image = ImageTk.PhotoImage(Image.open(hangman_images_dict[str(num_of_tries)]))
letters_guessed_label = Label(root, text='', bd=5, bg="white", font="Times 14")
status_bar = Label(root, text="You have {} guesses left".format(7 - num_of_tries), bd=5, relief=SUNKEN, anchor=E)
lose_or_win = Label(root, bg="white", font="Times 20 bold")
enter_button = Button(root)
invalid_input_label = Label(root, bg="white", font='Times 12 bold')
restart_button = Button(root, text="restart game", command=lambda: start_game())
hangman_frame = LabelFrame(root, text="Hangman", pady=5)
entry_box_label = Label(root, text="Guess a letter: ", bg="white", font="Times 12")
secret_word_label = Label(root, bg='white', font="Times 16", bd=5)
hangman_label = Label(hangman_frame)


# menu
my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu)
my_menu.add_cascade(label="game options", menu=file_menu)
file_menu.add_command(label="new game", command=lambda: start_game())
file_menu.add_command(label="exit", command=lambda: root.destroy())

root.mainloop()
