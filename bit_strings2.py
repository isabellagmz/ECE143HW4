# Isabella Gomez A15305555
# ECE143 HW4

# Instructions:
# Write a function map_bitstring that takes a list of bitstrings
# (i.e., 0101) and maps each bitstring to 0 if the number of 0s
# in the bitstring strictly exceeds the number of 1s. Otherwise,
# map that bitstring to 1. The output of your function is a
# dictionary of the so-described key-value pairs.

def map_bitstring(list_of_bits):
    '''
    This function takes in a list of bitstrings and returns a
    dictionary where the keys are the individual bitstrings, and
    the values are either 0 (when the bitstring has more 0s than
    1s) or 1 (when the bitsring has more 1s than 0s).

    :param list_of_bits: input list of bits to be parsed
    :return: dictionary with respective mappings
    '''

    # check that list of bits is only strings
    if len(list_of_bits) > 0:
        for element in range(len(list_of_bits)):
            assert type(list_of_bits[element]) == str
    else:
        return

    dictionary_map = {} # will hold all the bits and their values

    for entry in range(len(list_of_bits)):
        to_test = list_of_bits[entry] # stores entire entry
        counter_1 = 0 # counts how many 1s
        counter_0 = 0 # counts how many 0s

        # will count how many 1s and 0s in individual entry
        for bit in range(len(to_test)):
            if to_test[bit] == '1':
                counter_1 = counter_1 + 1
            elif to_test[bit] == '0':
                counter_0 = counter_0 + 1

        # compares the number of 1s and 0s
        if counter_0 > counter_1: # strictly greater than 1
            dictionary_map[to_test] = 0
        elif counter_1 >= counter_0:
            dictionary_map[to_test] = 1

    return dictionary_map
