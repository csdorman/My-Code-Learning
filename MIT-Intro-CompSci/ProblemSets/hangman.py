# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
      if char in letters_guessed:
        return True
      else:
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    word_display_list = []
    for char in secret_word:   # iterate through each character in secret word (list)
      if char in letters_guessed:
        word_display_list.append(char)     # if it's been guessed, append the character
      else:
        word_display_list.append("_ ")     # if it has not been guessed, print "_ "
    print(''.join(word_display_list))

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    unguessed_letters = set(string.ascii_lowercase).difference(letters_guessed)
    unguessed_letters = list(unguessed_letters)
    unguessed_letters.sort()
    return(print("Available letters: " + ''.join(unguessed_letters)))
    
def guess_validation(new_guess, guesses_left, letter_warnings, letters_guessed):
    '''
    new_guess: the newest letter that is guessed
    guesses_left: the number of incorrect guesses remaining
    letter_warnings: the number of non-letter warnings left
    letters_guessed: all of the letters that have been guessed so far

    Takes the new guess and makes sure that it is a letter.
    '''
    for char in new_guess:
      if char.isalpha():
        new_guess = new_guess.lower()
        print("Your guess: " + str(new_guess))
      else:
        print("That isn't a letter.")
        print("You've got " + str(letter_warnings) + " warnings left. Don't push me.")
        letter_warnings -= 1
        if letter_warnings <= 0:
          guesses_left -= 1
    letters_guessed.append(new_guess)
    return new_guess, guesses_left, letter_warnings, letters_guessed

def guess_result(new_guess, guesses_left):
    '''
    Takes the newest guess and sees if it is in the secret_word

    new_guess: the newest letter that is guessed
    guesses_left: the number of incorrect guesses remaining
    letter_warnings: the number of non-letter warnings left
    letters_guessed: all of the letters that have been guessed so far

    returns
    '''
    if new_guess in secret_word: # Is the new guess in the word?
      print("There is a letter " + str(new_guess) + " in the word!")
    else:
      print("Sorry. There is no letter " + str(new_guess) + " in the word.")
      guesses_left -= 1
      print("From guess_result else: " + str(guesses_left))

    return  guesses_left #new_guess


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''

    guesses_left = 6
    letter_warnings = 3
    letters_guessed = []
    print("Welcome to Hangman. You have been sentenced to die. Unless you correctly guess the word I am thinking of.")
    print("You have " + str(guesses_left) + " guesses left. Use them wisely")
    print("The mystery word has " + str(len(secret_word)) + " letters.")
    print("Letters to choose: " + string.ascii_lowercase)
    print("-----")

    turn = 1
    # First turn logic
    print(secret_word) # print secret word to see if code is correct
    print("==================")
    print("Turn Number: " + str(turn))
    new_guess = input("What letter do you choose?")
    guess_validation(new_guess, guesses_left, letter_warnings, letters_guessed)
    guesses_left = guess_result(new_guess, guesses_left) # See if guess is correct
    is_word_guessed(secret_word, letters_guessed) # See if word is guessed
    get_guessed_word(secret_word, letters_guessed) #Display letters + spaces
    turn = int(turn) + 1
    
    while is_word_guessed != True: #Successive turns
      print("==================")
      print("Turn Number: " + str(turn))
      print("You now have " + str(guesses_left) + " guesses left.")
      get_available_letters(letters_guessed) # Show letters not guessed
      new_guess = input("What letter do you choose?")
      guess_validation(new_guess, guesses_left, letter_warnings, letters_guessed)
      guesses_left = guess_result(new_guess, guesses_left) # See if guess is correct
      print("From hangman turn " + str(guesses_left))
      is_word_guessed(secret_word, letters_guessed) # See if word is guessed
      get_guessed_word(secret_word, letters_guessed) #Display letters + spaces
      turn = int(turn) + 1





    # Turn counter not decrementing below 1 
    
    # is_word_guessed needs to take into account turn counter (once fixed)

    # Game doesn't end even when correct word is guessed

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
