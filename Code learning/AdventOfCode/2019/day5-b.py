

#open intcode file
raw_data = open("diagnostic-code.txt", "r")
raw_data = raw_data.read()
#print(raw_data)
intcode_list = raw_data.split(',')
#turn intcode strings into integers
for i in range(len(intcode_list)):
    intcode_list[i] = int(intcode_list[i])

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

def mode(mode,position):
    val = 0
    #immediate mode
    if(mode == "1"):
        val = intcode_list[position]
    #parameter mode
    else:
        val = intcode_list[intcode_list[position]]
    return val

def intcode_computer(codes, input_num):
    counter = 0
    while counter < len(codes):
        opcode = codes[counter]
        if len(str(opcode)) < 5:
            opcode_inst = intcode_modes(opcode)
        #print(opcode_inst, type(opcode_inst))
        #print(counter)
        if opcode_inst[4] == "1":
            param1 = counter+1
            param2 = counter+2
            param3 = codes[counter+3]
            codes[param3] = mode(opcode_inst[2],param1) + mode(opcode_inst[1],param2)
            counter += 4
        elif opcode_inst[4] == "2":
            #print("Multiply")
            param1 = counter + 1
            param2 = counter + 2
            param3 = codes[counter + 3]
            codes[param3] = mode(opcode_inst[2],param1) * mode(opcode_inst[1],param2)
            counter += 4
        elif opcode_inst[4] == "3":
            #print(input)
            param1 = counter+1
            if opcode_inst[2] == "0":
                codes[codes[param1]] = input_num
            else:
                codes[param1] = input_num
            counter += 2
        elif opcode_inst[4] == "4":
            #print("output")
            param1 = counter + 1
            print(mode(opcode_inst[2], param1))
            counter += 2
        else:
            print("IF statements not reached")
            #print(codes)
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
   

#print(data("diagnostic-code.txt"))

intcode_computer(intcode_list, 1)


#print(param_mode(engage_computer("diagnostic-code.txt")))