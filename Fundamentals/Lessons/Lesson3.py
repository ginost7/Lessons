# there are if-elif-else, for & while loops, here are some scripts for you to
# copy and paste.  There are some exercises for you to do at the end

# 2 if-elif examples
# assign z to 4
z=4
if(z<70):
    print 'something is very wrong'
elif(z<7):
    print 'This is normal'
print ''
print '#####################################'
# assign i to -8
i = -8
if(i>0):
    print 'positive integer'
elif(i<0):
    print 'negative integer'
else:
    print 'zero'

print ''
print'####################################################################'
# if-elif-else example

# promt from the keyboard
x = int(raw_input("Please enter an integer: "))

if x < 0:
      x = 0
      print 'Negative changed to zero'
elif x == 0:
      print 'Zero'
elif x == 1:
      print 'Single'
else:
      print 'More'

print''
print '###############################################'

# This script changes the numbers of cars, people, and buses and
# trace through each if-statement to see what will be printed

people = raw_input("enter num of people: ") 
cars = raw_input("enter num of cars: ")
buses = raw_input("enter num of buses: ")


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."

print ''
print ''
###############################################################

# alternative ways to format the output of a for loop 
##define a list 
shuttles = ['columbia', 'endeavour', 'challenger', 'discovery', 'atlantis', 'enterprise', 'pathfinder' ]
 
## Read shuttles list and store the value of each element into s and display on screen
for s in shuttles:
        print s

print ''

## another way is to read shuttles list and enumerate into index and value 
for index, value in enumerate(shuttles):
        print index, value
print''        
#####################################################################
        
# nested for loop, we use the xrange function to save memory      
# try and test each loop by taking out a statement 
for x in xrange(1,5 ):
## Inner for loop	 ###
    for y in xrange(1, 5):
        print '%d ' % (x),
    print



print ''    
# nested for loop with an if-else statement
for num in range(10,20):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print '%d equals %d * %d' % (num,i,j)
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print num, 'is a prime number'
      
########################################################################
# example of while loop with if statement
# note we start with 10 down to 1, test it with a=100
a= 10
while a >0:
    print a
    if (a > 5):
        print "Big number!"
    elif ((a % 2) != 0):
        print "This is an odd number"
        print "It isn't greater than five, either"
    else:
        print "this number isn't greater than 5"
        print "nor is it odd"
        print "feeling special?"
    a = a - 1
    print "we just made 'a' one less than what it was!"
    print "and unless a is not greater than 0, we'll do the loop again."
################################################################################
#### program that asks you to guess a random number
    
import random                      # get the random library

number = random.randrange(1, 20) # Get random number between [1 and 1000)
guesses = 0
guess = int(input("Guess my number between 1 and 1000: "))

while guess != number:
    guesses += 1
    if guess > number:
        print(guess, "is too high.") 
    elif guess < number:
        print(guess, " is too low.")
    guess = int(input("Guess again: "))

print("\n\nGreat, you got it in", guesses,  "guesses!")
##### Excercise on loops
#####
########################################################################
# Ex3a

# write a program that uses a nested for loop to find the prime numbers from 2 to 100

# Ex3b

# what does this loop output?, Work it out before you run it

for i in range ( 1 ,100 ) :
    if i % 3 == 2 :
        print i , "mod" , 3 , "= 2"

# Ex3c
# use  iteratively the for loop to work out the factorial of a positive number from
# the interpreter prompt, examples are  3! = 3*2*1,   8! = 8*7*6*5*4*3*2*1








































































