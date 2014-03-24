# please note that the circle & rectangle modules are imported and
#IN SAME DIRECTORY AS THIS script FOR THIS TO WORK

import circle
import rectangle

def main():
    ''' choice variable controls the loop and the user menu'''
    choice = 0

    while choice != 5:
        # display the menu.
        display_menu()
        # Get the user's choice.
        choice = input ( ' Enter your choice : ' )
        # Perform the selected action.
        if choice == 1:
            radius = input("Enter the circle's radius: " )
            print 'The area is', circle.area(radius)
        elif choice == 2:
            radius = input( "Enter the circle's radius: " )
            print ' The circumference is ' ,  circle.circumference(radius)
        elif choice == 3:
                width = input("Enter the rectangle's width: " )
                length = input("Enter the rectangle's length: " )
                print 'The area is', rectangle.area(width, length)
        elif choice == 4:
                width = input("Enter the rectangle's width: " )
                length = input("Enter the rectangle's length: ")
                print 'The perimeter is ' , \
                        rectangle.perimeter(width, length)
        elif choice == 5:
                print 'Exiting the program . . . '
        else:
                print 'Error: invalid selection.'
# The display-menu function displays a menu.
def display_menu():
    print '         MENU '
    print ' 1) Area of a circle'
    print ' 2) Circumference of a circle '
    print ' 3) Area of a rectangle'
    print ' 4) Perimeter of a rectangle'
    print ' 5 ) Quit '
# Call the main function.
main ( )
        
