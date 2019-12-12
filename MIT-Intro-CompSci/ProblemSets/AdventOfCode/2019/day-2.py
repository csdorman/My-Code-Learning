
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
    # look at index pos 0 and every 4th index
    if index % 4 == 0:
        print("Index is", index)
        print("Opcode is", opcode)
        # opcode 1 means addition
        if opcode == 1:
            # get the values is opcode pos 1 and pos 2
            num1 = int(opcodes_list[int(opcodes_list[index + 1])])
            num2 = int(opcodes_list[int(opcodes_list[index + 2])])
            print("Num 1 is", num1, "index position", opcodes_list[index + 1])
            print("Num 2 is", num2,"index position", opcodes_list[index + 2])
            # calculate sum of opcode 1
            opcode_result = num1 + num2
            print("Opcode result", opcode_result)
            # find opcode save pos
            save_pos = int(opcodes_list[index + 3])
            print("Save position is", save_pos)
            # save opcode sum in save pos
            opcodes_list[save_pos] = opcode_result
            print("---")
        # opcdoe 2 means multiplication
        if opcode == 2:
            # get the values in opcode pos 1 and pos 2
            num1 = int(opcodes_list[int(opcodes_list[index + 1])])
            num2 = int(opcodes_list[int(opcodes_list[index + 2])])
            print("Num 1 is", num1)
            print("Num 2 is", num2)
            # calculate product of opcode 2
            opcode_result = num1 * num2
            print("Opcode result", opcode_result)
            # find opcode save pos
            save_pos = int(opcodes_list[index + 3])
            print("Save position is", save_pos)
            # save opcode product in save pos
            opcodes_list[save_pos] = opcode_result
            print("---")
        if opcode == 99:
            print("Program stopping")
            print("---")
            break