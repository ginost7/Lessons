
# ex3_1

for i in range(10):
    print( ' Hello ' )
##################################################################
# ex3_2

for i in range(3):
    num = eval(raw_input( ' Enter a number: ' ))
    print ( ' The square of your number is ' , num*num)
print( ' The loop is now done. ' )

##################################################################
# ex3_3
fruits = ['banana', 'apple', 'mango','strawberry','apples','kiwi']
for fruit in fruits:
        print 'Current fruit :', fruit

##################################################################
# ex3_4
# the following outputs the same result, depends on the problem which one
# you use

print "4 times table using while loop "
i = 1
while i <= 10:
    result = i * 4
    print i, "x 4 =", result
    i = i+1

print "4 times table using for loop"
for i in range (1,11):
    result = i * 4
    print i, "x 4 =", result
###########################################################################
    
#ex3_5

for letter in 'Python':
    print 'Current Letter :', letter

##########################################################################

#ex 3_6

for i in range(30):
    if not (i%3):
        continue
    print i

############################################################
print ''

# ex 3_7

def is_prime(num):
    for x in range(2, int(num**0.5)+1):
        if num % x == 0:
            return False
    return True

num = int(raw_input("Input any of the number you like:"))
if not is_prime(num):
    print "It is not a prime number"
else:
    print "It is a prime number"

###############################################

# ex3_9

   # Print a triangle of numbers like this:

#	1
#	1 2
#	1 2 3
#	1 2 3 4
#	1 2 3 4 5

for row in range(1, 6):
	for column in range(1, row + 1):
		print column,
	print

#################################################
    
