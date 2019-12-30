
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
    pw_options_increasing(pw_adjacent_options)
                
def pw_options_increasing(pw_adjacent_options):
    '''
    - Take the list from the previous problem
    - Check to make sure all numbers are increasing
    '''
    pw_possibilities = []
    for option in pw_adjacent_options:
        num_string = str(option)
        for index, num in enumerate(num_string):
            if num(index) > num(index + 1):
                pass
            else:
                pw_possibilities.append()
    print(len(pw_possibilities))

            
                

# pw_options_increasing should run first. It will eliminate more options quicker

password_options_adjacent(146810, 156810)