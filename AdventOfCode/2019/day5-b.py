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
    #print(intcode_list)
    while counter < len(intcode_list):
        opcode_inst = intcode_list[counter]
        param1 = intcode_list[counter+1]
        param2 = intcode_list[counter+2]
        param3 = intcode_list[counter + 3]
        #print("counter=",counter)
        #print("opcode_inst=",opcode_inst)
        #print("params. 1:",param1, "2",param2, "3",param3)
        #reading param and multi-digit intcodes
        #go to counter index in intcode list
        #take incode as a 6-digit STR
        #look at final 2 positions - get opcode from this
        #using enumerate to match index num with counter num
        for (index, intcode) in enumerate(intcode_list):
            #print("intcode=",intcode)
            if index == counter:
                intcode = str(intcode)
                print(counter, intcode)
                if str(intcode[-1]) == "1":
                    #add params
                    intcode_list[int(param3)] = int(param1) + int(param2)
                    #print("Opcode 1 triggered")
                    counter += 5
                elif str(intcode[-1]) == "2":
                    # multiply params
                    intcode_list[int(param3)] = int(param1) * int(param2)
                    counter += 5
                elif str(intcode[-1]) == "3":
                    # take input and save to only parameter 
                    intcode_list[int(param1)] = int(input_inst)
                    #print("Opcode 3 triggered")
                    counter += 2
                elif str(intcode[-1]) == "4":
                    # output the value of the only parameter
                    input_inst = param1
                    counter += 2
                else:
                    print("Counter:", counter, "Intcode:", intcode)
                    print("IF statement not reached")
                    counter += 1
            else:
                pass
    print(intcode_list[226])
    return intcode_list
   


opcode_func(param_mode(engage_computer("diagnostic-code.txt")), 1)


#print(param_mode(engage_computer("diagnostic-code.txt")))