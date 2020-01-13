# https://www.reddit.com/r/adventofcode/comments/e6carb/2019_day_5_solutions/

# open the diagnostic code file and load it into an array
input1 = open("diagnostic-code.txt", "r")
code = input1.read()
input1.close()
code = code.split(",")

# turn array elements into intergers
for i in range(len(code)):
    code[i] = int(code[i])

# return a five-element array to represent opcode
def opcodeArray(int1):
    opcode = list(str(int1))
    if len(opcode) < 5:
        for i in range(5-(len(opcode))):
            opcode.insert(0,"0")
    # turn back into intergers
    for i in range(len(opcode)):
        opcode[i] = int(opcode[i])
    return opcode

# find position of opcode to determine its function
def opcode_pos(opcode):
    for i in enumerate(opcode):
        #pos 3&4 are 2-digit opcode
        #pos 2 mode of param1
        #pos 1 mode of param2
        #pos 0 mode of param3
        print(i)

#define starting position
pos = 0

#keep going until opcode is 99
while(code[pos] != 99):
    num = opcodeArray(code[pos])
    print(num)
    pos += 1
        

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
    # turn array elements into intergers
    for i in range(len(opcodes_list)):
        opcode = int(opcode[i])
    #iterate through opcode list
    for opcode in opcodes_list:
        # need to add preceding 0s to opcodes of less than 5 digits.
        opcode = list(str(opcode))
        if len(opcode) < 5:
            for i in range(5-len(opcode)):
                opcode.insert(0,"0")
        for i in range(len(opcode)):
            opcode[i] = int(opcode[i])
        return opcode

        if opcode[-1] == 1:
            #stuff
            break
        if opcode[-1] == 2:
            #stuff
            break
        if opcode[-1] == 3:
            #stuff
            break
        if opcode[-1] == 4:
            #stuff
            break
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