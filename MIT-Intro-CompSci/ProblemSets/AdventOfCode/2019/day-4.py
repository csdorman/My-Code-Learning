
def password_options_adjacent(low, high):
    '''
    Find the password options between the two numbers
    
    password requirements:
    - range 146810 -> 612564
    - must have 2 adjacent digits that are the same
    - digits only increase going from L to R (0 is low)
    '''
    pw_adjacent_options = []
    for pw_options in range(146810, 156810):
        num_string = str(pw_options)
        index = 0
        for n in num_string:
            while index < 5:
                if num_string[int(index)] == num_string[int(index) + 1]:
                    pw_adjacent_options.append(num_string)
                else:
                    pass
                index = int(index)
                index += 1
    print(len(pw_adjacent_options))
    print(pw_adjacent_options)
                

#def password_options_increasing()

password_options_adjacent(146810, 612564)