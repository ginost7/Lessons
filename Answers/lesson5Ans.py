
# Answers to lesson 5

print '######################################################################'
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


print '#######################################################################'

import math

def print_results(sa, v): 
        ''' Print surface area and volume of a solid, with formatting'''
        print "The surface area is", round(sa, 2), "square meters"
        print "The volume is", round(v, 2), "cubic meters"

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
