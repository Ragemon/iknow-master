from math import sqrt
from itertools import count, islice

def primer():
    raw = int(input('Enter to check primality: '))
    if raw < 2:
        print(False)
    for number in islice(count(2), int(sqrt(raw) -1)):
        if raw % number == 0:
            print(False)
        else:
            print(True)


primer()












