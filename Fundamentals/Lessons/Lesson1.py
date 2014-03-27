#!/usr/bin/python
# -*- coding: utf-8 -*-

# Getting started
print(" *** Getting Started")
print("Hello world!")

# Boolean Types and Operators
print("\n *** Boolean Types and Operators")
x = True
y = False
print("x = True")
print("y = False")
print("x or y: {0}".format(x or y))
print("x and y: {0}".format(x and y))
print("x and not y: {0}".format(x and not y))

print("\n5 < 6: {0}".format(5 < 6))
print("5 <= 6: {0}".format(5 <= 6))
print("6 <= 6: {0}".format(6 <= 6))
print("5 > 6: {0}".format(5 > 6))
print("10 > 6: {0}".format(10 > 6))
print("6 >= 6: {0}".format(6 >= 6))
print("3 == 3: {0}".format(3 == 3))
print("4 != 3: {0}".format(4 != 3))

x = 3
print("\nx = 3")
print("x is 2: {0}".format(x is 2))
print("x is 3: {0}".format(x is 3))
print("x is x: {0}".format(x is x))

y = 3
print("\ny = 3")
print("x is y: {0}".format(x is y))
print("x is not 5: {0}".format(x is not 5))

print("\n *** Numeric Types")
import sys
print("sys.maxint: {0}".format(sys.maxint))
print("-sys.maxint – 1: {0}".format(-sys.maxint - 1))

x = 5
print("\nx = 5")
y = 3.4
print("y = 3.4")
print("x + y: {0}".format(x + y))
print("x - y: {0}".format(x - y))
print("y - x: {0}".format(y - x))
print("x * y: {0}".format(x * y))
print("x / y: {0}".format(x / y))
print("x // y: {0}".format(x // y))
print("x % y: {0}".format(x % y))
print("pow(x, y): {0}".format( pow(x, y) ))
print("x ** y: {0}".format(x ** y))

print("\n *** Sequence Types")
print("This is a string")
print('This is also a string')
#print("This is not a string')
print("Nathan's string")
print("\"This is a string,\" said Nathan.")

fruit = ["apple", "banana", "pear"]
print("\nfruit: {0}".format(fruit))
print("fruit[0]: {0}".format(fruit[0]))
print("fruit[1]: {0}".format(fruit[1]))
print("fruit[2]: {0}".format(fruit[2]))
print("The length of fruit is: {0}".format( len(fruit) ))

fruit.append('tomato')
print("\nfruit.append('tomato')")
print(fruit)

fruit[2] = "kiwi"
print("\nfruit[2] = 'kiwi'")
print(fruit)

fruit.pop(2)
print("\nfruit.pop(2)")
print(fruit)

fruit.append("kiwi")
fruit.append("pear")
print("\nfruit.append('kiwi')\nfruit.append('pear')\n{0}".format(fruit))

print("\nfruit[1:3]")
print(fruit[1:3])

print("\nfruit[0:len(fruit):2]")
print(fruit[0:len(fruit):2])

string = "A string"
print("\n{0}".format(string))

print("string[2:8]")
print(string[2:8])

print("\nstring[0:8:3]")
print(string[0:8:3])

print("\n *** Mapping Types")
numbers = {"one":1, "two":2, "three":3}
print(numbers)
print("The length of the dict numbes is: {0}".format( len(numbers) ))

print("\nnumbers['one']")
print(numbers['one'])

print("\nnumbers.get('one')")
print(numbers.get('one'))

numbers['four'] = 4
print("\nnumbers['four'] = 4")
print(numbers)

del numbers["three"]
print("\ndel numbers['three']")
print(numbers)

print("\n'five' in numbers")
print('five' in numbers)

print("\n'five' not in numbers")
print('five' not in numbers)

print("\nnumbers.keys()")
print(numbers.keys())

print("\nnumbers.values()")
print(numbers.values())

