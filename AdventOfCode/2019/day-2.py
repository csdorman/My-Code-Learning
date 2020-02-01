def open_file(file):
    '''
    Open a specific file and split into a list at ","
    '''
    opcodes = open(file)
    opcodes_raw = opcodes.read()
    opcodes_list = map(int, opcodes_raw.split(','))
    return list(opcodes_list)


def opcode_program(opcodes_list, noun, verb):
    '''
    Used to calculate the opcode result.   

    Opcode = 0, 1, or 99

    Index = The index position of the opcode. Used to find the other parameters based on their relation to the index number
    '''
    opcodes_list[1] = noun
    opcodes_list[2] = verb
    counter = 0
    while counter < len(opcodes_list):
        opcode = opcodes_list[counter]
        param1 = opcodes_list[opcodes_list[counter + 1]]
        param2 = opcodes_list[opcodes_list[counter + 2]]
        dest = opcodes_list[counter + 3]
        if opcode == 1:
            opcodes_list[dest] = param1 + param2
            counter += 4
        elif opcode == 2:
            opcodes_list[dest] = param1 * param2
            counter += 4
        elif opcode == 99:
            break
        else:
            print("Code unknown")
            break
    return opcodes_list[0]

def part_one():
    return opcode_program(open_file("opcode-list.txt"), 12, 2)

def part_two(output):
    '''
    Part two of Day 2
    '''
    opcodes_list = open_file("opcode-list.txt")
    for noun in range(100):
        for verb in range(100):
            if opcode_program(opcodes_list.copy(), noun, verb) == output:
                return 100 * noun + verb
    return "not found"

print(part_one())
print(part_two(19690720))
