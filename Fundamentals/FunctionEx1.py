
# define a function hello

def hello():
    print "hello"
    return 1234

print hello

# function that takes 2 arguments
def area(w, h):
    return w * h

print area(2,3) 
def print_welcome(name):
    print "Welcome", name
 
hello()
hello()
 
print_welcome("gino")
w = 4
h = 5
print "width =", w, "height =", h, "area =", area(w, h)
