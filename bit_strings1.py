# Isabella Gomez A15305555
# ECE143 HW4

# Instructions:
# Given a number of bits, write the get_sample function to return a
# list n of random samples from a finite probability mass function
# defined by a dictionary with keys defined by a specified number of
# bits. The values of the dictionary correspond of the probability
# of drawing any one of these.

import random
def get_sample(nbits=3,prob=None,n=1):
    '''
    This function takes in a dictionary of bits and probabilities and
    returns an n number of random samples from the keys of the dict.
    The size of the dictionary is dependent on the number nbits of
    digits given.

    :param nbits: the number of bits in the dictionary keys
    :param prob: dictionary of bits and probabilities
    :param n: length of return list
    :return: random_entry_list containing the n random samples taken
    '''

    # check that n and nbits are ints
    assert type(nbits) == int
    assert type(n) == int

    # check that prop is a dict if not NONE
    if prob != None:
        assert type(prob) == dict
        # check that the dictionary has the appropriate num of entries
        assert len(prob.keys()) == 2 ** nbits
    else:
        return

    total_entry_list = list(prob.items()) # contains all the dict entries as tuples
    random_entry_list = [] # will hold n number of entries from dict

    # will add the n random samples to the list
    for i in range(n):
        random_tuple = random.choice(total_entry_list)
        random_entry_list.append(random_tuple[0])

    return random_entry_list

