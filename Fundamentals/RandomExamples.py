
# uses of random library, run this several times and note the different o/p

import random

print random.choice(['apple', 'pear', 'banana'])

print random.sample(xrange(100), 10)   # sampling without replacement

print random.random()    # random float

print random.randrange(6)    # random integer chosen from range(6)
