
potentials = []
for i in range(146810,612564): 
    potentials.append(str(i))

passedfirst = []
for item in potentials:
    if list(item) == sorted(item):
        passedfirst.append(item)
                
passedsecond = []
for number in passedfirst:
    
    for digit in number:
            count = number.count(digit)
            if count >= 2: #change this to '==' for part 2 (srsly)
                passedsecond.append(number)               
                break  

print(len(passedsecond))


# def password_options_adjacent(pw_options_increasing):
#     '''
#     Find the password options between the two numbers
    
#     password requirements:
#     - range 146810 -> 612564
#     - must have 2 adjacent digits that are the same
#     - digits only increase going from L to R (0 is low)
#     '''
#     pw_adjacent_options = []
#     duplicate = True
#     #adjacent_digits = 1
#     #adjacent_high = 1
#     for option in pw_options_increasing:
#         num_str = str(option)
#         i = 0
#         adjacent_high = 0
#         adjacent_digits = 1
#         for n in num_str:
#             while i < 5:
#                 if int(num_str[i]) == int(num_str[i + 1]):
#                     duplicate = True
#                     adjacent_digits += 1
#                     if adjacent_digits >= adjacent_high:
#                         adjacent_high = adjacent_digits
#                     #print("Num 1 is", str(num_str[i]), "and Num 2 is", (str(num_str[i+1])), "they are equal. Duplicate =", duplicate)
#                     i += 1
#                 else:
#                     #print("Num 1 is", str(num_str[i]), "and Num 2 is", (str(num_str[i+1])), "they are NOT equal. Duplicate =", duplicate)
#                     duplicate = False
#                     adjacent_digits = 1
#                     i += 1
#         print(num_str, adjacent_high)
#         if adjacent_high == 2:
#             pw_adjacent_options.append(int(num_str))
#     return pw_adjacent_options
#     #print(pw_adjacent_options)
#     #print(len(pw_adjacent_options))               
# def pw_options_increasing(low, high):
#     '''
#     - Take the list from the previous problem
#     - Check to make sure all numbers are increasing
#     '''
#     pw_num_increasing = []
#     for option in range(low, high + 1):
#         num_str = str(option)
#         i = 0
#         increasing = True
#         while i < 5:
#             if num_str[i] > num_str[i + 1]:
#                 increasing = False
#                 break
#             else:
#                 i += 1
#         if increasing == True:
#             pw_num_increasing.append(int(num_str))
#     #print(len(pw_num_increasing))
#     return password_options_adjacent(pw_num_increasing)
#     #return pw_num_increasing
# num_list = pw_options_increasing(146810, 612564)
# print(num_list)
# print(len(num_list))