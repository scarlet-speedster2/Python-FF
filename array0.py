# If a list only contains numbers, an array.array is a more efficient replacement.
# Arrays support all mutable sequence operations (including .pop, .insert,
# and .extend), as well as additional methods for fast loading and saving, such
# as .frombytes and .tofile.


from array import array
from random import random
floats = array('d', (random() for i in range(10**7)))
print(floats[-1])
fp = open('floats.bin', 'wb')
floats.tofile(fp)
fp.close()
floats2 = array('d')
fp = open('floats.bin', 'rb')
floats2.fromfile(fp, 10**7)
fp.close()
floats2[-1]
print(floats2 == floats)
#print(floats2)