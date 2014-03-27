# more interesting loop scripts
# Use while loop as follows to run from 1 (i=1) to infinity
# The following will run infinity times 
i=1
while True:
    print "Welcome", i, "times. To stop press [CTRL+C]"
    i += 1


#####################################################################
#You can add delay using sleep() as follows, copy & paste this on a new
# window and change the delay times

import time
i=1
while True:
    print "Welcome", i, "times. To stop press [CTRL+C]"
    i += 1
    # Delay for 2 seconds
    time.sleep(2)

#####################################################################

#  infinte while loop 
# this example will go in an infite loop and you would need to use CTRL+C to come out of the program

var = 1
while var == 1 :  # This constructs an infinite loop
   num = raw_input("Enter a number  :")
   print "You entered: ", num

print "Good bye!"


# excercises


#ex4_1 access the keys in this dictionary

counts_dict = { 'chuck' : 1 , 'annie' : 42, 'jan': 100,'gino': 72}

# ex4_2

#find all the entries in the above dictionary with a value above ten

# ex4_3
#the program to compute an average without a list: 

