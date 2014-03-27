

## Answers

test = 'superCALifragilisticEXpialidocious'


print test.split('s')# takes the s out
print test.swapcase()
print test.upper()
print test.lower
print test.rjust(20) # add spaces to the left of string

##############################################################

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
print math_string.find('*') # where is the '*' character
print math_string.find('3')
print c.replace('i','o')    # replace i with o
print eval(math_string)     # gives us 11

############################################################

string1 = str(raw_input("type in the string: "))
print  ("The string is ", len(string1), "characters long")

#######################################################################


text = str(raw_input("type in some text: \n"))
number = int(raw_input("How many times should it be printed? "))
print(text * number)
#####################################################################

#Ex2_
# this checks if it is a palindrome

n=raw_input("Enter the String:")
def palindrome(n):
    index=0
    check=True
    while index<len(n):
        if n[index]==n[-1-index]:
            index+=1
            return True
        return False
if palindrome(n)==True:
    print "It is a Palindrome"
else:
    print "It is not a Palindrome"
