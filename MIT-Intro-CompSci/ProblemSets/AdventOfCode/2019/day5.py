# https://www.reddit.com/r/adventofcode/comments/e6carb/2019_day_5_solutions/

def open_file(file):
    opcodes = open(file)
    opcodes_raw = opcodes.read()
    opcodes_list = map(int, opcodes_raw.split(','))
    return list(opcodes_list)

def opcode_v2(opcodes_list):
    '''
    Used to calculate the opcode result.   
    V1:
    Opcode = 0, 1, or 99
    Index = The index position of the opcode. Used to find the other parameters based on their relation to the index number

    V2:
    Add support for: 
    Opcode 3 (takes a single integer as input and saves it to the position given by its only parameter), 4 (outputs the value of its only parameter)

    Modes: 
    Current opcode program is functioning in mode 0, position mode. If parameter is 50, the actual value of the parameter is *stored* at memmory position 50.
    Add support for mode 1 (immediate mode): If parameter is 50, its value is 50.
    Mode is stored in same value as opcode. Opcode is two-digit num in ones and tens place. Parameter modes are read R->L and each one digit number effects a single parameter.

    '''
    # need to add preceding 0s to opcodes of less than 5 digits.
    # parse the 5 digits to find opcodes and modes





    ##
    opcodes_list[1] = noun
    opcodes_list[2] = verb
    counter = 0
    while counter < len(opcodes_list):
        opcode = opcodes_list[counter]
        param1 = opcodes_list[opcodes_list[counter + 1]]
        param2 = opcodes_list[opcodes_list[counter + 2]]
        dest = opcodes_list[counter + 3]
        if opcode == 1:
            opcodes_list[dest] = param1 + param2
            counter += 4
        elif opcode == 2:
            opcodes_list[dest] = param1 * param2
            counter += 4
        elif opcode == 99:
            break
        else:
            print("Code unknown")
            break
    return opcodes_list[0]