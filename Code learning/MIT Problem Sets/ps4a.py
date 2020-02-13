# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    # if string list is 1, return single character
    if len(sequence) == 1:
        return [sequence]
    # create empty list
    perm_list = []
    # slice list from 2nd character to end
    for permutation in get_permutations(sequence[1:]):
        # iterate through each character in string
        for index in range(len(sequence)):
            # assemble permutation list
            perm_list.append(permutation[:index] + sequence[0:1] + permutation[index:])
        # pass list to next function call or return result
    return perm_list
       
        
if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))

# Test cases
    example_1 = "cat"
    print("Input:", example_1)
    print("Expected Output:", ['cat', 'act', 'atc', 'cta', 'tca', 'tac'])
    print("Actual Output:", get_permutations(example_1))

    example_2 = "tag"
    print("Input:", example_2)
    print("Expected Output:", ['tag', 'tga', 'atg', 'agt', 'gta', 'gat'])
    print("Actual Output:", get_permutations(example_2))

    example_3 = "bad"
    print("Input:", example_3)
    print("Expected Output:", ['bad', 'bda', 'abd', 'adb', 'dab', 'dba'])
    print("Actual Output:", get_permutations(example_3))

