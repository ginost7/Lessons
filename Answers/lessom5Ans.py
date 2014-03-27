
# lesson5 Answers
# Other ways of doing the examples but this my attempt, its a bit overkill
# but i hope you can understand them

print '#############################################################'

#ex5_1

def main():
    '''
    converts an input temperature in farenheit to celsius
    '''
    tempF = input("Input the temperature in Fahrenheit: ")
    tempC = (5.0/9.0) * (tempF - 32.0)
    print tempF, " F = ", tempC, " C"

main()

print '################################################################'

#Ex5_2

# Repeatedly read base & height of a triangle and print area.
# Ask user whether to continue.  Repeat if user says "yes"; stop if "no".

def triangle_area(base, height):
        area = 0.5 * base * height
        return area

option = "y"
while option == "y":
        base = float(raw_input("Base: "))
        height = float(raw_input("Height: "))
        print "The area is", triangle_area(base, height)
        option = raw_input("Another triangle?  (y/n) ")

print '##################################################################'

#Ex5_3

def day(name):
    '''
    this function determines whether you are 
    '''
    while True:
        day= raw_input('what day is it?: ')
        if name in ['Saturday', 'Sunday']:
            return 'weekend'
        elif name in ['Monday','Tuesday','wednesday','thursday','friday']:
            return 'weekday'
        else:
            return 'not a day'

print day('Monday')

print'###################################################################'

#ex5_6

import math

def print_results(sa, v): 
        # Print surface area and volume of a solid, with formatting
        print "The surface area is", round(sa, 2), "square inches"
        print "The volume is", round(v, 2), "cubic inches"

# Surface area and volume of a cube
height = float(raw_input("Height of cube: ")) 
surface_area = 6 * height ** 2
volume = height ** 3
print_results(surface_area, volume)

# Surface area and volume of a cylinder
height = float(raw_input("Height of cylinder: ")) 
radius = float(raw_input("Radius of cylinder: ")) 
area_of_base = math.pi * radius ** 2
surface_area = area_of_base * 2 + 2 * math.pi * radius * height
volume = area_of_base * height
print_results(surface_area, volume)

# Surface area and volume of a sphere
radius = float(raw_input("Radius of sphere: ")) 
surface_area = 4.0 * math.pi * radius ** 2
volume = (4.0 / 3.0) * math.pi * radius ** 3
print_results(surface_area, volume)

print '#################################################################'

'''
here is a mostly-straightforward solution to the
4 by 4 grid. Please note the careful use of the functions
'''

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print '+ - - - -',

def print_post():
    print '|        ',

def print_beams():
    do_twice(print_beam)
    print '+'

def print_posts():
    do_twice(print_post)
    print '|'

def print_row():
    print_beams()
    do_four(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()


