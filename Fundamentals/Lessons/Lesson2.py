
# this lesson is on strings copy & paste the print statements on to the interpreter 
# use single quotes. Answer the first 4 questions
print 'welcome to the python language'

# use can also use double quotes
print "welcome to the python language"

# note the quotes must match
#  print 'welcome to the python language" WILL GIVE YOU AN ERROR

# adding strings

print 'Albert ' + 'Einstein'

# this is an empty string
print ''

# you can use the * operator BUT NOT THE + operator 
print 'CT' * 5

# using multilne strings  . PLEASE NOTE NEWLINE IS OS DEPENDENT

print ' one\ntwo\nthree\tfour'

print '\n'

# format the print to test what you require
print 'one\ttwo\nthree\tfour'

# basically anything can go here if you use triple quotes
print ''' cgdsu\ncgsuycbcusd'cbb'isd
hbsdcd"sdcs\tdbc"sdjh
cbcbcjhsdchjsdhdhs'''

print ''
# string formatting using %f,%d and %s
elephants = 3
gorillas = 2
snakes = 12
s = 'great'
print 'there are %f elephants, %f gorillas, %d snakes and its %s ' %(elephants,gorillas,snakes,s)

print ''

# assign s  a string
s = 'Hi there python i think its a very practical language to learn, you can do great things with it'

print s[0]

print s[2]

print s[7]

print ''


# slicing the s  string

print s[1:9]
print s[4:24]

print ''

# import the string module

import string

print ''

# find number of t letters in s
print s.find('t')
print ''
#split() function breaks a string down into substrings. Note string is an object
# access method using object.method() ie s.split(''), s.lower(), s.upper()
print s.split(' ')
print ''
print s.lower()

print ''
print s.upper()

# new line
print ''

# look at the outputs of the following, using string functions which are in string library
s= 'welcome to the python class'
print s
print len(s)
print s
# the result is true
print s.islower()
# the result is false
print s.isupper()
s3 = s.center(11)
print''
print''
print''
print''
print''
print''

#####################   EXERCISES  ##########################################

#ex2_1
# lets manipulate this well known string
test = 'supercalifragilisticexpialidocious'

# there are quite a few string functions in the string library
# what do you think the output to the following is? test them after :

print test.split('s')
print test.swapcase()
print test.upper()
print test.lower
print test.rjust(20) 


############################################################

#ex2_2
# examples of manipulating the  library strings methods, find out what the print
# statements do and test them at the prompt

a= "my first test string"
b= "another test string is created"
c= "this string belongs to gino"
d= 'my favourite vegetable  is " carrots" what is yours?'
math_string = "3+4*2"
express_string = "a' + '+b+'  tiger"



print len(a)            # length a
print len(math_string)  # length of math_string
print a+b               # concatenate 2 strings
print b+a               # this does the same in the other way
print math_string + express_string   # another string add
print b.split('t')      # splits the string at t
print math_string.find('*') # where is the 8 character
print math_string.find('3')
print c.replace('i','o')    # replace i with o
print eval(math_string)     # gives us 11

####################################################################
#ex2_3
# Write a script that asks the user to type in a string and tells the user how
# long that string is

########################################################################

#ex2_4
# write a script that asks the user for a string, then a number. It then
# prints out the string that many times
#################################################################

#ex2_5
# ask the user to input a string and check if its a palindrome




