

# open opcodes file
def data(raw_data):
    raw_data = open(raw_data, "r")
    raw_data = raw_data.read()
    intcode_list = map(int,raw_data.split(','))
    return list(intcode_list)

def intcode_modes(opcode):
    #intcodes_list = list(map(str, intcode_list))
    opcode = str(opcode)
    leading_zero = "0"
    intcode = []
    #print(code, len(code), "Too short")
    for i in range(5-len(opcode)):
        opcode = leading_zero + opcode
        #print(code)
    intcode.append(opcode)
    return(opcode)

def mode(mode,position,code):
    val = 0
    #parameter mode
    if(mode == 0):
        val = code[code[postion]]
    #immediate mode
    else:
        val = code[position]
    return val

def intcode_computer(codes, input_num):
    counter = 0
    while counter < len(codes):
        opcode = codes[counter]
        if len(str(opcode)) < 5:
            opcode_inst = intcode_modes(opcode)
        print(opcode_inst, type(opcode_inst))
        if opcode_inst[-1] == "1":
            #print("Add")
            param1 = counter+1
            param2 = counter+2
            param3 = codes[counter+3]
            param3 = mode(opcode_inst[2],param1,codes) + mode(opcode_inst[1],param2,codes)
            counter += 4
        elif opcode_inst[-1] == "2":
            #print("Multiply")
            param1 = counter + 1
            param2 = counter + 2
            param3 = codes[counter + 3]
            param3 = mode(opcode_inst[2],param1,codes) * mode(opcode_inst[1],param2,codes)
            counter += 4
        elif opcode_inst[-1] == "3":
            #print(input)
            param1 = counter+1
            if opcode_inst[2] == "0":
                codes[codes[param1]] = input_num
            else:
                codes[param1] = input_num
            counter += 2
        elif opcode_inst[-1] == "4":
            #print("output")
            param1 = counter + 1
            print(mode(opcode_inst[2], param1))
            counter += 2
        else:
            print("IF statements not reached")
            print(codes)
            break



# define different opcode instructions
def opcode_func(intcode_list, input_inst):
    counter = 0
    #print(intcode_list)
    while counter < len(intcode_list):
        #set opcode to counter
        opcode_inst = str(intcode_list[counter])
        #set params to operate by default in position mode
        param1 = int(intcode_list[counter+1])
        param2 = int(intcode_list[counter+2])
        param3 = int(intcode_list[counter+3])
        for opcode in intcode_list:
            opcode_inst = intcode_modes(opcode_inst)
        if str(opcode_inst[-1]) == "1":
            #addition
            intcode_list[param3] = int(mode_value(opcode_inst[2], param1, intcode_list)) + int(mode_value(opcode_inst[1], param2, intcode_list))
            #print("Opcode 1 triggered")
            counter += 4
        elif str(opcode_inst[-1]) == "2":
            # multiply params
            intcode_list[param3] = int(mode_value(opcode_inst[2], param1, intcode_list)) * int(mode_value(opcode_inst[1], param2, intcode_list))
            counter += 4
        elif str(opcode_inst[-1]) == "3":
            # take input and save to only parameter 
            intcode_list[param1] = int(input_inst)
            #print("Opcode 3 triggered")
            counter += 2
        elif str(opcode_inst[-1]) == "4":
            # output the value of the only parameter
            input_inst = param1
            counter += 2
        else:
            print("Counter:", counter, "Intcode:", opcode_inst)
            print("IF statement not reached")
            counter += 1
    return intcode_list
   

print(data("diagnostic-code.txt"))
intcode_computer(data("diagnostic-code.txt"), 1)


#print(param_mode(engage_computer("diagnostic-code.txt")))