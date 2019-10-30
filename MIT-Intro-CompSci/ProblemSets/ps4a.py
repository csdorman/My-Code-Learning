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
            perm_list.append()
       
        # add to end of string
        # code examples here: https://stackoverflow.com/questions/13109274/python-recursion-permutations
        # recursive
        # take index 1 (2nd char) of list, add +1 to index num (WHY 2nd char?)
        # 
        #
    pass #delete this line and replace with your code here

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

