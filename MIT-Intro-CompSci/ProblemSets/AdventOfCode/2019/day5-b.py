

# open opcodes file
def engage_computer(raw_data):
    raw_data = open(raw_data, "r")
    raw_data = raw_data.read()
    intcode_list = map(int,raw_data.split(','))
    return list(intcode_list)

def param_mode(intcode_list):
    intcodes_list = list(map(str, intcode_list))
    leading_zero = "0"
    intcodes = []
    for code in intcodes_list:
        if len(code) < 5:
            #print(code, len(code), "Too short")
            for i in range(5-len(code)):
                code = leading_zero + code
                #print(code)
            intcodes.append(code)
    return(intcodes)

# define different opcode instructions
def opcode_func(intcode_list, input_inst):
    counter = 0
    print(len(intcode_list))
    while counter < len(intcode_list):
        opcode = intcode_list[counter]
        param1 = intcode_list[int(intcode_list[counter+1])]
        param2 = intcode_list[int(intcode_list[counter+2])]
        param3 = intcode_list[counter + 3]
        if opcode == 1:
            # add params
            intcode_list[param3] = param1 + param2
            print("Opcode 1 triggered")
            counter += 4
        elif opcode == 2:
            # multiply params
            intcode_list[param3] = param1 * param2
            counter += 4
        elif opcode == 3:
            # take input and save to only parameter 
            intcode_list[param1] = input_inst
            counter += 2
        elif opcode == 4:
            # output the value of the only parameter
            return intcode_list[param1]
            counter += 2
        else:
            break
        return intcode_list


print(opcode_func(param_mode(engage_computer("diagnostic-code.txt")), 1))
