# # Isabella Gomez A15305555
# # ECE143 HW4
#
# # Instructions: From gather_values, we can group the results
# of the random samples. Now, we want to threshold those values
# based upon their frequency and value. Given threshold=2, we
# want to keep only those bitstrings with the two highest frequency
# counts of the 1 value.

def threshold_values(seq,threshold=1):
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
        assert type(bit) == str

    # check that the threshold is int
    assert type(threshold) == int



    return
