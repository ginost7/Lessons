# function using main() and returning values and start using docstrings
# to document code. Bit over the top to find square root but illustrates the
#point

import math

def main():
    ''' demonstrates docstring to document the code'''
    # user inputs a number
    number = input('Enter a number: ')

    # get a square root of a number
    square_root = math.sqrt(number)

    # display the answer

    print 'the square root of ', number, 'is', square_root

# note we are calling main(), its a keyword
main()

