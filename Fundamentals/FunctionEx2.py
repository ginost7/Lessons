# a user input script using functions with input values being positive

def hello():
    print 'Hello!'
 
def area(width, height):
    return width * height
 
def print_welcome(name):
    print 'Welcome,', name
 
name = raw_input('Your Name: ')
hello(),
print_welcome(name)

print 'To find the area of a rectangle,'
print 'enter the width and height below.'

w = input('Width: ')
while w <= 0:
    print 'Must be a positive number'
    w = input('Width: ')
 
h = input('Height: ')
while h <= 0:
    print 'Must be a positive number'
    h = input('Height: ')
 
print 'Width =', w, 'Height =', h, 'so Area =', area(w, h)
