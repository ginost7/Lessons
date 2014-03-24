
# this lesson is on strings copy & paste the print statements on to the interpreter 
# use single quotes
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

# ex1
# here are 4  strings s1,s2,s3 and s4, what are the outputs of the print statements?

s1 = 'i love python, its fantastic language to learn'
s2 = s1
s3 = 'i love python, its fantastic language to learn'
s4 = 'yes'

#a)print s1 == s2
#b)print s2.count('o')
#c)print id(s1) == id(s2)
#d)print id(s1) == id(s3)
#e)print s1<= s4
#f)print s2>= s4
#g)print s1!= s4
#h)print s1.upper()
#i)print s2.find(s4)
#j)print s1[4]
#k)print s1[4:8]
#l)print 4* s4
#m)print len(s1)
#n)print max(s1)
#o)print min(s1)
#p)print s1[-4]
#q)print s1.lower()
#r)print s1.rfind('o')
#s)print s1.startswith("o")
#t)print s1.endswith("o")
#u)print s1.isalpha()
#v)print s1+s2
#w)print ((s1 + ' oh my god!\n') * 3)

#############################################################################
#ex2
# what does the following  for loops 'string traversal 'print out?
#a)
#
#for achar in 'hi these exercies are easy!':
#    print(achar)
#
#b)
#
#for ListName in ['joe','gino','lino','omar','putin','boris','gordon']:
#    invite = 'hi there ' + ListName + '.  lets get together for a code session!'
#    print(invite)
#
#############################################################################
#ex3
#
#What is printed by the following statements?
#s = "ball"
#r = ""
#for item in s:
#    r = item.upper() + r
#print(r)
#
#############################################################################
#ex4
#
#Write a program from the python prompt that checks if a string is palindrome or not
#
#ex5
# What is the output of this program? 
#
#vowels = "aeiou"
#for v in vowels:
#  if v in "uranium":
#      print v
#
#
                  






