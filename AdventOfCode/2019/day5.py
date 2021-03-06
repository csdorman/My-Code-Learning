
#open intcode file
raw_data = open("diagnostic-code.txt", "r")
raw_data = raw_data.read()
intcode_list = raw_data.split(',')

#turn intcode strings into integers
for i in range(len(intcode_list)):
    intcode_list[i] = int(intcode_list[i])

#turn all opcodes into 5 digits
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

#get intcode mode (parameter/immediate) based on opcode
def mode(mode,position):
    val = 0
    #immediate mode
    if(mode == "1"):
        val = intcode_list[position]
    #parameter mode
    else:
        val = intcode_list[intcode_list[position]]
    return val

#run computer
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
    
intcode_computer(intcode_list, 1)