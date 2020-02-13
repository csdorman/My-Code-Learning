# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

# HELPER CO


def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

# END HELPER CODE

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    '''
    Docstring
    '''
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words('words.txt')


    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        self.get_message_text = message_text
        return self.get_message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.

        Returns: a COPY of self.valid_words
        '''
        self.get_valid_words = valid_words.copy()
        return self.get_valid_words

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        # import string library
        import string
        # create empty alphabet_list variable
        self.alphabet_list = []
        # save lower and upper case to list
        self.alphabet_list = string.ascii_lowercase
        # create empty dictionary
        self.shift_dict = {}
        letter_index = 0
        # for each letter in alphabet_list
        for letter in self.alphabet_list:
            # save real letter to variable
            self.real_letter = letter
            # find cipher letter
            if letter_index + shift >= 26:
                self.cipher_letter = self.alphabet_list[letter_index + (shift - 26)]
            else:
                # print("Letter index =", letter_index)
                # print("Shift =", shift)
                self.cipher_letter = self.alphabet_list[letter_index + shift]
            # save real and cipher letters to shift_dict
            self.shift_dict[self.real_letter] = self.cipher_letter
            letter_index += 1
        # print(self.shift_dict)
        return self.shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        import string
        self.alphabet_list = string.ascii_lowercase
        # empty list for converted message
        self.shifted_message = []
        # for each character in the message list
        print(self.message_text)
        print(self.shift)
        for letter in self.message_text:
            print(letter)
            # if character is a space or punctuation
            if letter not in self.alphabet_list:
                self.shifted_message.append(letter)
            # else send to shift_dict
            else:
                for letter in self.shift_dict.keys():
                    cipher_letter = self.shift_dict[letter]
                    self.shifted_message.append(cipher_letter)
        # convert shifted_message list into string
        self.shifted_message_string = ''.join(self.shifted_message)
        return self.shifted_message_string


class PlaintextMessage(Message):
    '''
    Docstring
    '''
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object

        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        # Use super() method to use Message parent class defs
        #super().__init__(Message)
        # Other defs
        self.message_text = text
        self.valid_words = load_words('words.txt')
        self.shift = shift
        self.encryption_dict = Message.build_shift_dict(self, shift)
        print("Shift =", shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class

        Returns: self.shift
        '''
        self.get_shift = self.shift
        return self.get_shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class

        Returns: a COPY of self.encryption_dict
        '''
        self.get_encryption_dict = self.get_encryption_dict.copy()
        return self.get_encryption_dict

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class

        Returns: self.message_text_encrypted
        '''
        self.get_message_text_encrypted = self.message_text_encrypted
        return self.get_message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other
        attributes determined by shift.

        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.change_shift = input("What is your shift amount?")
        self.shift = self.change_shift


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object

        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.valid_words = load_words('words.txt')

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create
        the maximum number of valid words, you may choose any of those shifts
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        #start shift testing at 1 (not 0)
        shift_num = 1
        #list for decryption dicts
        decrypt_lists = []
        # iterate from 1 to 26
        for shift_num in range(27):
            #send to apply_shift (this def iterates through letters)
            decrypt_try = Message.apply_shift(26 - shift_num)
            print(decrypt_try) #print for testing
            # split decrypt_try at spaces
            word_check = decrypt_try.split()
            #iterate through (potential) words
            word_counter = 0
            for word in word_check:
                # check if they are real words
                is_word(self.valid_words, word)
                if is_word == True:
                    #count the number of real words
                    word_counter += 1
            #store results in dict
            new_shift = {
                'shift' : shift_num,
                'message' : decrypt_try,
                'valid_words' : word_counter,
            }
            #store dict result in a list
            decrypt_lists.append(new_shift)
        max_word_count = max(decrypt_lists, key=lambda x:x['valid_words'])
        max_word_shift = max_word_count.get('shift')
        max_word_message = max_word_count.get('message')
        return max_word_message, max_word_shift


if __name__ == '__main__':

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
    #Test cases
    plaintext_1 = PlaintextMessage('hello', 4)
    print('Expected output: lipps')
    print('Actual output:', plaintext_1.get_message_text_encrypted)

    plaintext_2 = PlaintextMessage('hello word', 4)
    print('Expected output: lipps asvh')
    print('Actual output:', plaintext_2.get_message_text_encrypted)

#    Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    #ciphertext_1

    #ciphertext_2

    #TODO: best shift value and unencrypted story

    pass #delete this line and replace with your code here
