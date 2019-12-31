
def password_options_adjacent(low, high):
    '''
    Find the password options between the two numbers
    
    password requirements:
    - range 146810 -> 612564
    - must have 2 adjacent digits that are the same
    - digits only increase going from L to R (0 is low)
    '''
    pw_adjacent_options = []
    for pw_options in range(146810, 612564):
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
        num_str = str(option)
        i = 0
        increasing = True
        while i < 5:
            if num_str[i] > num_str[i + 1]:
                increasing = False
                break
            else:
                i += 1
        if increasing == True:
            pw_possibilities.append(num_str)
    print(len(pw_possibilities))





    #     index = 0
    #     for num in range(len(num_string)):
    #         #print("Index", index, type(index), "and num", num, type(num))
    #         if num < num[index + 1]:
    #             index += 1
    #             print(num_string)
    # #         while index < 6:
    # #             if int(num[index]) > int(num[index + 1]):
    # #                 increasing = False
    # #                 pass
    # #             else:
    # #                 index += 1
    # #         if increasing != False:
    # #             increasing = True
    # #             pw_possibilities.append(option)
    # # print(len(pw_possibilities))
                

# pw_options_increasing should run first. It will eliminate more options quicker

password_options_adjacent(146810, 612564)