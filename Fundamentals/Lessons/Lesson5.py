# examples of functions

# Below is the function
def hello():
    ''' function that does something. Note this is a docstring comment'''
    print "hello"
    return 1234

# And here is the function being used
print hello()

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
print 'We use *args and **kwargs to collect extra arguments and extra keyword arguments:'

def show_args(x, y=-1, *args, **kwargs):
    print '-' * 40
    print 'x:', x
    print 'y:', y
    print 'args:', args
    print 'kwargs:', kwargs

def test():
    show_args(1)
    show_args(x=2, y=3)
    show_args(y=5, x=4)
    show_args(4, 5, 6, 7, 8)
    show_args(11, y=44, a=55, b=66)

test()


####################################################################
## Excercises
####################################################################

#ex5a

#ex5b

#ex5c

#ex5d

