#open intcode file
raw_data = open("test-data.txt", "r")
raw_data = raw_data.read()
intcode_list = raw_data.split(',')

#turn intcode strings into integers
for i in range(len(intcode_list)):
    intcode_list[i] = int(intcode_list[i])
#print(intcode_list)

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
    #position mode
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
        elif opcode_inst[4] =="5":
            param1 = counter + 1
            param2 = counter + 2
            #jump if true
            if mode(opcode_inst[2],param1) != 0:
                counter = mode(opcode_inst[1],param2)
            else:
                counter += 3
        elif opcode_inst[4] =="6":
            param1 = counter + 1
            param2 = counter + 2
            #jump if false
            if mode(opcode_inst[2],param1) == 0:
                counter = mode(opcode_inst[1],param2)
            else:
                counter += 3
        elif opcode_inst[4] =="7":
            param1 = counter + 1
            param2 = counter + 2
            param3 = codes[counter +3]
            #less than
            if mode(opcode_inst[2],param1) < mode(opcode_inst[1],param2):
                codes[param3] = 1
            else:
                codes[param3] = 0
            counter += 4
        elif opcode_inst[4] =="8":
            param1 = counter + 1
            param2 = counter + 2
            param3 = codes[counter +3]
            #equals
            if mode(opcode_inst[2],param1) == mode(opcode_inst[1],param2):
                codes[param3] = 1
            else:
                codes[param3] = 0
            counter += 4
        else:
            #print("IF statements not reached")
            #print(codes)
            break
    
intcode_computer(intcode_list, 5)