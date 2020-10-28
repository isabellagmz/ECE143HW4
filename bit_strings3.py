# Isabella Gomez A15305555
# ECE143 HW4

# Instructions:
# Now that you have get_sample working, generate n samples and
# tally the number of times an existing key is repeated. Generate
# a new dictionary with bitstrings as keys and with values as
# lists that contain the corresponding mapped values from
# map_bitstring.

def gather_values(x):
    '''
    This function takes in a list from get_sample and count how many
    elements are repeated in the sample and whether they have more
    ones or zeros in it.

    :param x: input from get_sample
    :return: dictionary with
    '''

    # check all elements in x are strings
    for bits in range(len(x)):
        assert type(x[bits]) == str

    # Following 20 lines makes a bitstring dictionary
    bitstring_map = {} # will hold all the bits and their values

    for entry in range(len(x)):
        to_test = x[entry] # stores entire entry
        counter_1 = 0 # counts how many 1s
        counter_0 = 0 # counts how many 0s

        # will count how many 1s and 0s in individual entry
        for bit in range(len(to_test)):
            if to_test[bit] == '1':
                counter_1 = counter_1 + 1
            elif to_test[bit] == '0':
                counter_0 = counter_0 + 1

        # compares the number of 1s and 0s
        if counter_0 > counter_1:  # strictly greater than 1
            bitstring_map[to_test] = 0
        elif counter_1 >= counter_0:
            bitstring_map[to_test] = 1

    map_dict = {} # dictionary that will contain mapping

    # dict of unique elements and their map
    mapping_keys = list(bitstring_map.keys())
    mapping_vals = list(bitstring_map.values())

    # check how many times an element in x is repeated
    for element in range(len(mapping_keys)):
        list_of_maps = [] # contains all 1s or all 0s
        for i in range(len(x)):
            # add a 1 or 0 for everytime an element is repeated
            if mapping_keys[element] == x[i]:
                list_of_maps.append(mapping_vals[element])
        # after counting repetitions, add it to dictionary
        map_dict[mapping_keys[element]] = list_of_maps

    return map_dict
