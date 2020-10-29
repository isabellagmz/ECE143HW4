# Isabella Gomez A15305555
# ECE143 HW4

# Instructions:
# Write a generator that tracks the output of this producer and ultimately
# returns the number of odd numbered seconds
# that have been iterated over.

from time import sleep
import random
from datetime import datetime
import math
import itertools as it

def producer():
    'produce timestamps'
    starttime = datetime.now()
    while True:
        sleep(random.uniform(0, 0.2))
        yield datetime.now() - starttime


def tracker(p,limit):
    '''
    This is a genetator increments a counter everytime the time ellapsed
    between the creation of producer and the execution is odd. It does
    this until it reaches the given limit. Tracker also receives new limit
    input.

    :param p: the output of producer in datetime format
    :param limit: number at which counter stops
    :yield: the number of iterations it took to reach limit
    '''

    # check that limit is an int
    assert type(limit) == int

    # to call producer
    p = producer()

    # call producer until we reach the limit
    ellapsed_seconds = 0
    count = 0

    while count != limit:
        ellapsed_seconds = math.floor(next(p).total_seconds())
        if ellapsed_seconds % 2 == 0:
            yield count
        elif ellapsed_seconds % 2 != 0:
            count = count + 1
            yield count
