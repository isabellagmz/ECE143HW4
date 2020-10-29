# # Isabella Gomez A15305555
# # ECE143 HW4
#
# # Instructions: From gather_values, we can group the results
# of the random samples. Now, we want to threshold those values
# based upon their frequency and value. Given threshold=2, we
# want to keep only those bitstrings with the two highest frequency
# counts of the 1 value.

def threshold_values(seq,threshold=2):
    '''
    This function will take a list of bits and check which ones have
    mostly 1s and which ones have mostly 0s. Then, it will return a
    dictionary that contains the bits as keys. Its values are going
    to be either 1 or 0 depending on whether the bit has more ones or
    more zeroes. However, there can only be 'threshold' amounts of 1s,
    if there are more, then the ones that are most repeated will be
    the ones and the others will all become zeroes.

    :param seq: the list of bits coming in that will be parsed
    :param threshold: the number of keys whose value will remain 1
    :return: dictionary with keys and their 1s or 0s
    '''

    # check that seq has all str
    for bit in range(len(seq)):
        assert type(seq[bit]) == str

    # check that the threshold is int
    assert type(threshold) == int
    assert threshold != 0

    # Following 20 lines makes a bitstring dictionary
    bitstring_map = {}  # will hold all the bits and their values

    for entry in range(len(seq)):
        to_test = seq[entry]  # stores entire entry
        counter_1 = 0  # counts how many 1s
        counter_0 = 0  # counts how many 0s

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

    map_dict = {}  # dictionary that will contain mapping

    # dict of unique elements and their map
    mapping_keys = list(bitstring_map.keys())
    mapping_vals = list(bitstring_map.values())

    repeated = 0  # how many times a bit is repeated

    # check how many times an element in x is repeated
    for element in range(len(mapping_keys)):
        list_of_maps = []  # contains all 1s or all 0s
        for i in range(len(seq)):
            # add a 1 or 0 for everytime an element is repeated
            if mapping_keys[element] == seq[i]:
                list_of_maps.append(mapping_vals[element])
        # after counting repetitions, add it to dictionary
        map_dict[mapping_keys[element]] = list_of_maps

    repeated_keys = list(map_dict.keys()) # list with all the keys
    repeated_vals = list(map_dict.values()) # list with all the values

    # will have list of longest length
    repeated_ones_dict = {}

    for val in range(len(repeated_vals)):
        # makes 0s into 0
        if repeated_vals[val][0] == 0:
            map_dict[repeated_keys[val]] = 0
        # store the ones into a new dictionary
        for i in range(len(repeated_keys)):
            if repeated_vals[val][0] == 1:
                repeated_ones_dict[repeated_keys[val]] = len(repeated_vals[val])

    # sort the dictionary from smallest to biggest
    sorted_dict_by_key = {}
    sorted_dict_by_value = {}

    repeated_ones_keys = list(repeated_ones_dict.keys())
    #repeated_ones_keys.sort()
    #print(repeated_ones_keys)

    '''for key in sorted(repeated_ones_dict.keys()):
        sorted_dict_by_key[key]=repeated_ones_dict[key]
    sorted_keys = list(sorted_dict_by_key.values())
    sorted_keys.sort(reverse=True)
    print(sorted_dict_by_key)
    print(sorted_keys)'''

    sorted_dict_by_value = sorted(repeated_ones_dict.items(), key=lambda x: x[1], reverse=True)
    print(sorted_dict_by_value)

    # change to 1 if threshold is bigger than possible 1s
    if threshold >= len(sorted_dict_by_value):
        for key in range(len(sorted_dict_by_value)):
            map_dict[sorted_dict_by_value[key][0]] = 1

    while threshold != 0:
        for key in range(len(sorted_dict_by_value)):
            map_dict[sorted_dict_by_value[key][0]] = 1
        threshold = threshold - 1

    return map_dict
