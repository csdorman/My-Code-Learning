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
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
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
    # convert to lower case
    word = word.lower()
    # add letter values (given above) together
    letter_sum = 0
    for char in word:
        if char in SCRABBLE_LETTER_VALUES:
            letter_sum += SCRABBLE_LETTER_VALUES[char]
    # find greater value - 1 OR 7 * word_len - 3 *(n-word_len)
    length_sum = 7 * len(word) - 3 *(n - len(word))
    if length_sum > 1:
    #multiply first and second components together, retur result
        return letter_sum * length_sum
    else:
        return letter_sum * 1
    
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
    
    for letter in hand:
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
        #NEED TO MODIFY CONSTANT AT TOP?
        if "*" not in hand: #check for a wildcard
            hand["*"] = 1 #add one if not present
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
    #create copy of hand to keep original
    new_hand = dict(hand)
    word = word.lower()
    #convert word string to dictionary
    get_frequency_dict(word)
    #iterate through letters in word
    for char in word:
        #if word letter in hand dictionary
        if char in new_hand:
            #remove one instance from new_hand
            new_hand[char] -= 1
        else:
            continue
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
    word = word.lower()  # convert word into lower case
    valid_letter = None
    valid_word = None
    
    if "*" in word: #Is wildcard support needed?
        for letter in VOWELS: #Yes
            wildcard_word_valid = word.replace("*", letter)
            if wildcard_word_valid in word_list:
                valid_word = True
            else:
                continue
        word = get_frequency_dict(word) #convert word into a dict
        for char in word:
            if char in hand and hand[char] >= word[char]: #is char in hand and are their enough
                valid_letter = True
            else:
                valid_letter = False
                break
    
    else: #No
        if word in word_list: 
            valid_word = True #check if word in word_list
            word = get_frequency_dict(word) #convert word into a dict
            for char in word:
                if char in hand and hand[char] >= word[char]: #is char in hand and are their enough
                    valid_letter = True
                else:
                    valid_letter = False
                    break
        else: 
            valid_word = False

    if valid_letter == True and valid_word == True:
        #print("Valid letter is", valid_letter, "and valid word is", valid_word)
        return True
    else:
        #print("Valid letter is", valid_letter, "and valid word is", valid_word)
        return False

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    hand_len = 0
    for letter in hand:
        hand_len += 1
    return hand_len

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
    
    # Keep track of the word and hand score
    word_score = 0
    hand_score = 0
    current_hand_size = calculate_handlen(hand)
    #if hand is empty, end 
    if current_hand_size > 0:
        display_hand(hand)
        #ask user to input word
        word = input("Enter word, or '!!' to finish this hand: ")
        #check to see if '!!' is entered
        while word != "!!":
            #update hand to remove used letters
            hand = update_hand
            #use is_valid_word to test word
            is_valid_word(word, hand, word_list)
            if is_valid_word == True:
                #get and display word score
                word_score = get_word_score(word,  HAND_SIZE)
                print("Good job. That word earned", word_score, "points.")
                hand_score += word_score
                word = input("Enter word, or '!!' to finish this hand: ")
            if is_valid_word == False:
                print("That is not a valid word. Try again")
                word = input("Enter word, or '!!' to finish this hand: ")
            #show updated hand
            display_hand(hand)
    else:
        pass
    print("Good game. Your total score for this hand was", hand_score)
        

    

#OLD VERSON
    # Ask user for input
    # word = input("Enter word, or '!!' to indicate that you are finished: ") 
    # # If the input is two exclamation points
    #  word == "!!":  # End the game (break out of the loop)
    #     print("Game over!") #Game over, return score
    #     print("Total score:", total_score, "points")
    #     return(total_score) # Return the total score as result of function
    # else: # Otherwise (the input is not two exclamation points):
    #      # If the word is valid:
    #     is_valid_word(word, hand, word_list)
    #     print("Is_valid_word function returns", is_valid_word)
    #     if is_valid_word == True:
    #         word_score = 0
    #         for char in word:
    #             word_score += dict.get(char)
    #         total_score = word_score + total_score
    #                         # Tell the user how many points the word earned, and the total score
    #         print(word, "earned", word_score, "points. Total:", total_score)
    #     else:  # Otherwise (the word is not valid):
    #         print("That is not a valid word. Please choose another word") # Reject invalid word (print a message)
    #     # update the user's hand by removing the letters of their inputted word
    #     hand = update_hand(hand, word)
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
    letter_to_replace = letter
    #make sure that letter is in the users hand
    if letter_to_replace in hand:
        #get value of letter in hand
        number = letter_to_replace.get()
        #combine these into one list
        all_letters = CONSONANTS + VOWELS
        #pick random letter from list
        new_letter = random.choice(all_letters)
        #create new_hand dict to avoid mutating orignal hand
        new_hand = hand
        #if first random choice is already in hand, choose again
        while new_letter in new_hand:
            new_letter = random.choice(all_letters)
        else:
            hand.pop(letter_to_replace)
            new_hand[new_letter] = number
    else:
        new_hand = hand
    return new_hand

       
    
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
    #set game score, word score, and hand score to zero
    game_score = 0
    hand_score = 0
    word_score = 0
    #set game counter to zero
    game_counter = 0
    #set sub_letter and replay_hand to False
    sub_letter = False
    replay_hand = False
    #ask player for desired number of hands
    game_number = input("How many hands would you like to play?")
    #deal_hand function
    hand = deal_hand(HAND_SIZE)
    #display_hand function
    display_hand(hand)
    #check if sub_letter has been used
    #if not used yet, ask if user would like to sub letter
    if sub_letter == False:
        sub_letter_conf = input("Would you like to substite a letter, yes/no?")
        if sub_letter_conf.lower() == "yes":
            letter = input("What letter would you like to replace?")
            hand = substitute_hand(hand, letter)
        else:
            pass
    else:
        pass
    #GAME LOOP BEGINS
    play_hand(hand, word_list)
    # while word != "!!":
    #     #is_valid_word function to validate word
    #     is_valid_word(word, hand, word_list)
    #     #if is_valid_word returns True, send to get_word_score
    #     if is_valid_word == True:
    #         word_score = get_word_score(word, calculate_handlen)
    #         #add word score to hand score
    #         hand_score += word_score
    #         #display word score to user
    #         print(word, "earned", word_score, "points. Total", hand_score, "points.")
    #     #update hand to remove the used letters
    #     hand = update_hand(hand, word)
    #     #display new hand
    #     display_hand(hand)
    #     #ask user to play a word
    #     word = input("Please entera word, or '!!' to indicate you are done.")
    # LOOP END - when "!!" entered or letters run out
    #increment game counter +1
    game_counter += 1
    #display hand score to user
    print("Your score for that hand was", hand_score)
    #add hand score to game score
    game_score += hand_score
    #check if game counter = number of games
    if game_counter == game_number:
        #if games done, print out game score
        print("Good game! Your total score was", game_score)
    else:
        #reset hand score to 0
        hand_score = 0

    #if more games needed, continue

    print("play_game not implemented.") # TO DO... Remove this line when you implement this function
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
