# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    #convert word string into lower case
    word = word.lower()
    #get word length
    wordlen = len(word)
    #create empty variables
    word_score = 0
    letter_sum = 0
    second_component = 0
    #iterate through word letters 
    for char in word:
        #add values of letters together
        letter_sum += SCRABBLE_LETTER_VALUES.get(char, 0)
    #find value of second component
    second_component = 7 * wordlen - 3 *(n - wordlen)
    #take greater of second component value or 1, multiple two comp together
    if second_component > 0:
        word_score = letter_sum * second_component
    else: 
        word_score = letter_sum * 1
    #return product
    return word_score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

        
    for i in range(num_vowels):
        if '*' not in hand:
            hand['*'] = hand.get('*', 0) + 1    
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # copy hand into new_hand variable (dict.copy)
    new_hand = hand.copy()
    #convert word into lowercase
    word = word.lower()
    # convert word into dict
    word_dict = get_frequency_dict(word)
    # iterate through letters in word
    for word_char in word_dict:
        char_value = 0
        hand_value = 0
        # get value of each letter - save to variable
        char_value = word_dict.get(word_char, 0)
        # iterate through letters in new_hand
        if word_char in hand:
            # get value of each letter
            hand_value = hand.get(word_char, 0)
        else: 
            continue
        # subtract word value from new_hand value
        new_hand[word_char] = hand_value - char_value
        #if letter value falls below 0, set it to 0
        if new_hand[word_char] < 0:
            new_hand[word_char] = 0
    #return new_hand
    return new_hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    #convert word to lowercase
    word = word.lower()
    #check for presence of wildcard
    if "*" in word:
        wildcard_valid = wildcard_integration(word, word_list)
        if wildcard_valid == True:
            char_in_hand = are_char_in_hand(word, hand)
            if char_in_hand == True:
                return True
    if word in word_list:
        char_in_hand = are_char_in_hand(word, hand)
        if char_in_hand == True:
            return True
    else:
        return False

def wildcard_integration(word, word_list):
    """
    If wildcard found in guess, iterate through possible vowel substitutions to see if the word is is_valid_word

    word = string
    word_list = list of lowercase strings
    return = boolean
    """
    is_wildcard_guess_valid = None
    for char in VOWELS:
        wildcard_guess = word.replace("*", char)
        if wildcard_guess in word_list:
            is_wildcard_guess_valid = True
            break
        else:
            is_wildcard_guess_valid = False
    return is_wildcard_guess_valid

def are_char_in_hand(word, hand):
    """
    Checking to make sure all the letters in the played word are in the player's hand

    word = string
    hand = dict
    return = boolean
    """
    valid_play = None
    #convert word string into dict
    word = get_frequency_dict(word)
    #iterate through word char
    for char in word:
        word_value = 0
        hand_value = 0
        #get value of each char in played word
        word_value = word.get(char, 0)
        #get value of same char in hand
        hand_value = hand.get(char, 0)
        #make sure hand contains enough char to play the word
        if hand_value >= word_value:
            valid_play = True
        else: 
            valid_play = False
            break
    return valid_play

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    hand_length = 0
    for char in hand:
        hand_length += 1
    return hand_length

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    # Keep track of the total score
    total_score = 0
    # As long as there are still letters left in the hand:
    hand_length = calculate_handlen(hand)
    while hand_length >= 1:
        # Display the hand
        display_hand(hand)
        # Ask user for input
        word = input("Enter word, or '!!' to indicate that you are finished: ")
        # If the input is two exclamation points:
        if word == "!!":
            # End the game (break out of the loop)
            break           
        # Otherwise (the input is not two exclamation points):
        else:
            player_word_valid = is_valid_word(word, hand, word_list)
            # If the word is valid:
            if player_word_valid == True:
                # Tell the user how many points the word earned,
                word_score = get_word_score(word, hand_length)
                total_score = total_score + word_score
                # and the updated total score
                print("That word got", word_score, "points. Your total score is now", total_score)
            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print("Your word is not valid. Please enter another word or enter '!!' to quit.")
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, word)
    # Game is over (user entered '!!' or ran out of letters),
    print("Game over!")
    # so tell user the total score
    print("Good game. Your final score was", total_score)

    # Return the total score as result of function
    return total_score


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    # ask user if they want to sub a letter
    want_letter_sub = input("Would you like to substitute a letter? (yes/no)")
    # if yes
    if want_letter_sub == "yes":
        # ask which letter to substitute
        letter_to_sub = input("Which letter would you like to substitute?")
        # if letter is in their hand
        #create updated_hand variable for modified hand
        updated_hand = hand
        if letter_to_sub in updated_hand:
            # pick a new letter from VOWELS and CONSONANTS at random
            full_alphabet = VOWELS + CONSONANTS
            new_letter = random.choice(full_alphabet)
            # while letter is in hand
            while new_letter in updated_hand:
                # draw a new letter
                new_letter = random.choice(full_alphabet)
            updated_hand[new_letter] = updated_hand.pop(letter_to_sub)
            # return new hand
            return updated_hand
        # if letter is not in their hand
        else:
            pass
    # if no
    else:
        pass
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    print("play_game not implemented.") # TO DO... Remove this line when you implement this function
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
