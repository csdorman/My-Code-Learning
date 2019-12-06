
def opcode_calc(opcode, num1, num2, save_pos):
    '''
    Used to calculate the opcode result
    '''
    if opcode == 99:
        exit
    elif opcode == 1:
        save_pos = num1 + num2
        return save_pos
    elif opcode == 2:
        save_pos = num1 * num2
        return save_pos

# open text file
opcodes = open("opcode-list.txt")
# read text file 
opcodes_raw = opcodes.read()
# split at ","
opcodes_list = []
opcodes_list = opcodes_raw.split(",")
#print(opcodes_list) #Getting the raw opcode_list for debugging
# use enumerate in order to relate a specific opcode to its index
for index, opcode in enumerate(opcodes_list):
    opcode = int(opcode)
    if index == 0:
        print(opcodes_list[0:5]
        #print("Opcode at index", index, "is", opcode)
        #run opcode_calc function
        # NEED TO PASS IT CURRENT OPCODE AND NEXT FEW ALSO
        func_result = opcode_calc()
        func_result = opcodes_list[3]
        print(opcodes_list[0:5]
    #elif (index % 4) == 0: 
        #run opcode_calc function