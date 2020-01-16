

# open opcodes file
def engage_computer(raw_data):
    intcode_list = map(int,raw_data.split(','))
    return list(intcode_list)

# define different opcode instructions
def opcode_func(intcode_list):
    counter = 0
    while counter < len(intcode_list):
        opcode = intcode_list[intcode_list[counter]]
        param1 = intcode_list[intcode_list[counter+1]]
        param2 = intcode_list[intcode_list[counter+2]]
        dest = intcode_list[counter + 3]
        #print(counter, opcode, param1, param2, dest)
        if opcode == 1:
            # add params
            intcode_list[dest] = param1 + param2
            counter += 4
        elif opcode == 2:
            # multiply params
            intcode_list[dest] = param1 * param2
            counter += 4
        elif opcode == 3:
            # take input and save to only parameter
            intcode_list[dest] = param1
            counter += 2
        elif opcode == 4:
            # output the value of the only parameter
            return intcode_list[dest]
            counter += 2
        elif opcode == 99:
            break
        else:
            print("Unknown code")
    return intcode_list


print(opcode_func(engage_computer("1,0,0,0,99")))