# -*- coding: utf-8 -*-
# examples of functions copy and paste them to check your answer

# Below is the function
def hello():
    ''' function that does something. Note this is a docstring comment'''
    print "hello"
    return 1234

# And here is the function being used at the prompt, 
print hello()

## this draws a square

def draw_square():
    print( ' * ' * 15)
    print( ' * '  * 11)
    print( ' * ' * 15)

print ''

print draw_square()

###########################################################################
print''
## functions can have any type of loop structure AND take arguments or not as follows

def greet(lang):
    if lang == 'es':
        print 'Hola'
    elif lang == 'fr':
        print 'Bonjour'
    else:
         print 'Hello'

## try different greet inputs, note that the arguments will  be in string formats

greet('es')
print ''
greet('en')
print ''
greet('fr')
print ''


## adding parameters into the function

def add(x,y):
    return x+y

print add(2,3)

# Functions can also be called using arguments of the form keyword = value:

def player(name, number, team="rangers"):
   print(name + "wears number " + str(number) + "for " + team)
   
# call the  function

print player("Gino", 23)

print''
print '#########################################################'

print ''

# function that takes 2 numbers and determines which is the max

def max(num1,num2):
    if (num1>num2):
        result = num1
    else:
        result = num2
    return result

# lets call the function, please look at the logic of the function

print max(9,18)




#Functions can be called from within functions:

# lets take the function max() and use it using main()[A KEYWORD FUNCTION]

def main():
    i = 5
    j = 2
    k = max(i,j) # call the max function
    print("The larger the number of ", i, "and ", j,"is",k)

# lets call main()

main()
    

def square(x): 
    return x*x  # note, one can also use x**2 for x squared, 
                # x**3 for x cubed, x**4 for x^4 and so on...

def to_the_power_of_four(x):       
        return square(x) * square(x) # gets x^2^2 (i.e. x^4)

print to_the_power_of_four(3)

####################################################################
## Excercises
####################################################################

#ex5_1
# write a function that converts farhenheit to celsius

#ex5_2
# write a function that asks the user the height and base length of a triangle and then calculates 
# the area of that triangle remember to use A = 1/2* base*height

#ex5_3
# write a function that determines if a day is either a weekend OR a weekday (hint use
# 2 lists and if-elif statements. Also use raw_input 
 

#ex5_4
# The following code implements two mutually recursive functions – functions which call
# each other, what is the output of the print statements?

#def ise(n):
#    if n==0:
#        return True
#    else:
#        return iso(n-1)
#def iso(n):
#    if n==0:
#        return False
#    else:
#        return ise(n-1)


print iso(3)
print iso(2)
print ise(3)
print ise(2)


#ex5_5  write a function that calculates the surface area and volume of a cube, cylinder and sphere
# use import math for the pi value

#ex 5_6 write a program that creates the following grid system hint lots of functions with  statements 

#+---------+--------+
#|         |        |
#|         |        |
#|         |        |
#|         |        |
#+---------+--------+
#|         |        |
#|         |        |
#|         |        |
#|         |        |
#+---------+--------+
