from bit_strings1 import get_sample
from bit_strings2 import map_bitstring as map
from bit_strings3 import gather_values as gather
from bit_strings4 import threshold_values as threshold
from coroutines import tracker
from coroutines import producer

class Homework4:
    def __init__(self):
        pass

if __name__ == '__main__':

    my_Homework4 = Homework4()
    # get_sample()
    list_given = ['100', '001', '111']
    # print(map(list_given))
    p = {'000': 0.125, '001': 0.125, '010': 0.125, '011': 0.125,
         '100': 0.125, '101': 0.125, '110': 0.125, '111': 0.125}
    # print(get_sample(prob=p,n=5))
    samples = get_sample(prob=p,n=20)
    # print(samples)
    # print(gather(samples))
    # print(threshold(samples))

    p = producer()
    t = tracker(p, limit=3)
    next(t)
    #print(list(tracker(p,limit=5)))
    #for i in range(5):
        #print(list(tracker(p, 5)))
    #print(next(p))

