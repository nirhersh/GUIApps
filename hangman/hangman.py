def open_screen():
    """this func prints to the screen the open screen"""
    HANGMAN_ASCII_ART = ("""     _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                        |___/
    6""")      #6 is the max tries
    print (HANGMAN_ASCII_ART)

def choose_word(file_path, index):
    """this func gets the words file for the game and an index number. the func returns the word the player will need to guess.
    :param file_path: the files file path
    :param index: an index number from the player
    :type file_path: str
    :type index: str
    :return: a tuple that contains the word to guess
    :rtype: tuple
    """
    words_object = open(file_path, 'r')
    num_index = int(index) - 1
    list_of_words = []
    for line in words_object:
        words_list = line.split(' ')
        for word in words_list:
            if '\n' in word:
                new_word = word[:-1]
                words_list.remove(word)
                words_list.append(new_word)
        list_of_words.extend(words_list)
    if num_index <= len(list_of_words):
        guess_word = list_of_words[num_index]
        return guess_word
    else:
        corrected_num_index = num_index - len(list_of_words)
        guess_word = list_of_words[corrected_num_index]
        return guess_word
    words_object.close()

def print_hangman(num_of_tries):
    """this func prints the correct hangman situation according to the num of failed tries.
    :param num_of_tries: the number of failed tries by the player
    :type num_of_tries: int
    :return: none
    """
    hangman_photos = {'0': "x-------x", '1': ":(\nx-------x\n|\n|\n|\n|\n|", '2': ":(\nx-------x\n|       |\n|       0\n|\n|\n|", '3': ":(\nx-------x\n|       |\n|       0\n|       |\n|\n|", '4': ":(\nx-------x\n|       |\n|       0\n|      /|\\ \n|\n|", '5': ":(\nx-------x\n|       |\n|       0\n|      /|\\ \n|      /\n|", '6': ":(\nx-------x\n|       |\n|       0\n|      /|\\ \n|      / \\ \n|"}
    print(hangman_photos[str(num_of_tries)])

def underscore_word(guess_word):
    """this func returns the initial underscore word in the start of the game
    :param guess_word: the word that the player need to guess
    :type guess_word: str
    :return: none
    """
    length_of_word = len(guess_word)
    underscore_word = str(guess_word).replace(str(guess_word), ' _ ' * length_of_word)
    return underscore_word
    
def is_letter_right(letter_guessed_lower, guess_word):
    """this function determines if the letter guessed is correct or not
    :param letter_guesed_lower: the letter guessed lower
    :param guess_word: the word to guess
    :type letter_guesed_lower: str
    :type guess_word: str
    :return: True or False
    :rtype: bool
    """
    if letter_guessed_lower in guess_word:
        return True
    else:
        return False

def show_hidden_word(guess_word, old_letters_guessed):
    """this function return the hidden word with the letters that have been guessed
    :param guess_word: the secret word
    :param old_letters_guessed: the letters that have been gussed already
    :guess_word type: string
    :old_letters_guessed type: list
    :return: the hidden word
    :rtye: string
    """
    hidden_word_list =[]
    for x in guess_word:
        if x not in old_letters_guessed:
            hidden_word_list.append(' _ ')
        else:
            hidden_word_list.append(x)
        hidden_word = ' '.join(hidden_word_list)
    return hidden_word

def check_valid_input(letter_guessed_lower, old_letters_guessed):
    """ this function determines if the letter guessed by the player is valid or not
    :param letter_guesed_lower: the letter that was guessed by the player
    :param old_letters_guessed: a list of all the letters that has already been guessed
    :type letter_guesed_lower: str
    :type old_letters_guessed: list
    :return: answer
    :rtype: bool
    """
    letter_guessed_length = len(letter_guessed_lower)
    if letter_guessed_length > 1:
        return False
    elif letter_guessed_lower not in "abcdefghijklmnopqrstuvwxyz":
        return False
    elif letter_guessed_lower in old_letters_guessed:
        return False
    else:
        old_letters_guessed.append(letter_guessed_lower)
        return True

def try_update_letter_guessed(letter_guessed_lower, old_letters_guessed):
    """this function help the player remember wich letters he has guessed already
    :param letter_guesed_lower: the letter that was guessed by the player
    :param old_letters_guessed: a list of all the letters that has already been guessed
    :type letter_guesed_lower: str
    :type old_letters_guessed: list
    :return: a string to print
    rtype: str
    """
    letter_guessed_length = len(letter_guessed_lower)
    if letter_guessed_length > 1:
        return "You can't enter more than one letter"
    elif letter_guessed_lower not in "abcdefghijklmnopqrstuvwxyz":
        return "You entered a character that is not a letter "
    else:
        old_letters_guessed.sort()
        return 'You already guessed that one'

def check_win(guess_word, old_letters_guessed):
    """this function checks if the player has won or not
    :param guess_word: the word the user need to guess
    :param old_letters_guessed: the list of all the guessed letters
    :type guess_word: str
    :type old_letters_guessed: list
    :return: True or False
    :rtype: bool
    """
    guess_word_list = list(guess_word)
    check_list = []
    for x in guess_word:
        if x in old_letters_guessed:
            check_list.append(x)
    check_list.sort()
    guess_word_list.sort()
    if guess_word_list == check_list:
        return True
    else:
        return False

def main():
    num_of_tries = 0
    old_letters_guessed = []
    open_screen() #displays open screen
    file_path = input("enter the file path: ") #argument for choose_word
    index = input("enter index number: ") #argument for choose_word
    guess_word = choose_word(file_path, index) #returns guess_word
    print("Let's start!")
    print_hangman(num_of_tries) #the first photo of hangman
    show_underscore_word(guess_word) #shows the initial underscore word
    while num_of_tries < 7:
        win = check_win (guess_word, old_letters_guessed)
        if win == False:
            letter_guessed = input ("guess a letter: ")#a letter the user guesses
            letter_guessed_lower = letter_guessed.lower() #lowered letter for the func
            input_valid = check_valid_input(letter_guessed_lower, old_letters_guessed) #determines if the input is valid
            if input_valid == False:
                try_update_letter_guessed(letter_guessed_lower, old_letters_guessed) #prints if not valid according to the func
            else:
                letter_right = is_characte_right(letter_guessed_lower, guess_word) #determine if letter is in the guess_word
                if letter_right == True:
                    show_hidden_word(guess_word, old_letters_guessed) #if letter is correct it prints the hidden word
                else:
                    num_of_tries += 1
                    print_hangman(num_of_tries) #if letter not correct prints the next hangman photo
                    show_hidden_word(guess_word, old_letters_guessed) #shows the hidden word
        else:
            print("YOU WIN")
            break
        if num_of_tries == 6:
            print("YOU LOSE")
            break

if __name__ == "__main__":
    main()