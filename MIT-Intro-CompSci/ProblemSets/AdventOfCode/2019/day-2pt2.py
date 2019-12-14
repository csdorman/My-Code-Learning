

def opcode_calc(opcode, index):
    '''
    Used to calculate the opcode result.
    
    Opcode = 0, 1, or 99
    Index = The index position of the opcode. Used to find the other parameters based on their relation to the index number
    '''
    if opcode == 99:
        return opcodes_list[0]
    elif opcode == 1:
        # get the values is opcode pos 1 and pos 2
        param1 = int(opcodes_list[int(opcodes_list[index + 1])])
        param2 = int(opcodes_list[int(opcodes_list[index + 2])])
        #print("Parameter 1 is", param1, ", at index position", opcodes_list[int(opcodes_list[index + 1])])
        #print("Parameter 2 is", param2,", at index position", opcodes_list[int(opcodes_list[index + 2])])
        # calculate sum of opcode 1
        opcode_result = param1 + param2
        #print("Opcode result", opcode_result)
        # find opcode save pos
        save_pos = int(opcodes_list[index + 3])
        #print("Save position is", save_pos)
        # save opcode sum in save pos
        opcodes_list[save_pos] = opcode_result
        return opcodes_list[0]
        #print("---")
    elif opcode == 2:
         # get the values in opcode pos 1 and pos 2
        param1 = int(opcodes_list[int(opcodes_list[index + 1])])
        param2 = int(opcodes_list[int(opcodes_list[index + 2])])
        #print("Parameter 1 is", param1)
        #print("Parameter 2 is", param2)
        # calculate product of opcode 2
        opcode_result = param1 * param2
        #print("Opcode result", opcode_result)
        # find opcode save pos
        save_pos = int(opcodes_list[index + 3])
        #print("Save position is", save_pos)
        # save opcode product in save pos
        opcodes_list[save_pos] = opcode_result
        return opcodes_list[0]
        #print("---")

def noun_verb_iter ():
    '''
    Used to iterate through the opcode_lists positions 1 and 2 number.

    Both pos 1 and 2 must start at 0 and iterate through ALL combinations.
    '''
    noun = []
    verb = []
    for x in range(100):
        noun.append()
        verb.append()
    combined = [(noun, verb) for x in noun for y in second] 
    print(combined)


# open text file
opcodes = open("opcode-list.txt")
# read text file 
opcodes_raw = opcodes.read()
# split at ","
opcodes_list = []
opcodes_list = opcodes_raw.split(",")
noun = 0
verb = 0
#print(opcodes_list) #Getting the raw opcode_list for debugging
# use enumerate in order to relate a specific opcode to its index
while opcodes_list[0] != 19690720:
    opcodes_list = opcodes_raw.split(",")
    opcodes_list[1] = noun
    opcodes_list[2] = verb
    if noun == verb:
        noun += 1
    else: 
        verb += 1
    for index, opcode in enumerate(opcodes_list):
        opcode = int(opcode)
        #look at index pos 0 and every 4th index
        if index % 4 == 0:
            #print("Index is", index)
            #print("Opcode is", opcode)
            opcode_calc(opcode, index)
    print(opcodes_list[0])
print(opcodes_list[0:5])