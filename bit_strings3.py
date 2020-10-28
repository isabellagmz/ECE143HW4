# Isabella Gomez A15305555
# ECE143 HW4

# Instructions:
# Now that you have get_sample working, generate n samples and
# tally the number of times an existing key is repeated. Generate
# a new dictionary with bitstrings as keys and with values as
# lists that contain the corresponding mapped values from
# map_bitstring.

from bit_strings2 import map_bitstring
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

    print(x)
    map_dict = {} # dictionary that will contain mapping

    # dict of unique elements and their map
    mapping_keys = list(map_bitstring(x).keys())
    mapping_vals = list(map_bitstring(x).values())

    print(mapping_keys)
    print(mapping_vals)
    # check how many times an element in x is repeated
    for element in range(len(mapping_keys)):
        list_of_maps = []
        for i in range(len(x)):
            if mapping_keys[element] == x[i]:
                list_of_maps.append(mapping_vals[element])
        map_dict[mapping_keys[element]] = list_of_maps

    return map_dict
