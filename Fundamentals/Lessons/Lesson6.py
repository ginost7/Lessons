# -*- coding: utf-8 -*-
# lesson on classes,

# create a Box class

# The __init__ method is special. It is a constructor.
#Init receives parameters and assigns fields to the new class instance.

class Box:
    def area(self):
        return self.width * self.height

    def __init__(self, width, height):
        self.width = width
        self.height = height

# Create an instance of Box.
x = Box(10, 2)

# Print area.
print(x.area())
####################################################################

# create a Point class first attempt

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

#So let’s use our new Point class now:

p = Point()         # Instantiate an object of type Point
q = Point()         # Make a second point

print(p.x, p.y, q.x, q.y)  # Each point object has its own x and y

# the program prints  0000
#because during the initialization of the objects,
#we created two attributes called x and y for each, and gave them both the value 0.

#########################################################################

# second attempt for point class


class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y


p = Point(4, 2)
q = Point(6, 3)
r = Point()       # r represents the origin (0, 0)
print(p.x, q.y, r.x)

##########################################################################

# adding distance_from_origin method to the class

class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


#let’s create a few point instances, look at their attributes,
# and call our new method on them:

p = Point(3, 4)
p.x
p.y
p.distance_from_origin()
q = Point(5, 12)
q.x
q.y
q.distance_from_origin()
r = Point()
r.x
r.y
r.distance_from_origin()
#############################################################################

# create a Person class

class Person:
    def sayHi(self):
        print'Hello,how are you?'

p = Person()
print p
	          
        
p = Person() # create an p object
print p

# modify the class so that it has a constructor def __init__(self, name)
#
#Just like the __init__ method, there is another special
#method __del__ which is called when an object is going to die i.e.
#it is no longer being used and is being returned to the system for
#reusing that piece of memory.
#In this method, we simply decrease the Person.population count by 1. 
class Person:
	'''Represents a person.'''
	population = 0

	def __init__(self, name):
		'''Initializes the person's data.'''
		self.name = name
		print '(Initializing %s)' % self.name

		# When this person is created, he/she
		# adds to the population
		Person.population += 1
	
	def __del__(self):
		'''I am dying.'''
		print '%s says bye.' % self.name

		Person.population -= 1

		if Person.population == 0:
			print 'I am the last one.'
		else:
			print 'There are still %d people left.' % Person.population
	
	def sayHi(self):
		'''Greeting by the person.
		
		Really, that's all it does.'''
		print 'Hi, my name is %s.' % self.name
	
	def howMany(self):
		'''Prints the current population.'''
		if Person.population == 1:
			print 'I am the only person here.'
		else:
			print 'We have %d persons here.' % Person.population


gino = Person('Gino') # initialises the Person class
gino.sayHi()
gino.howMany()

print ''

Politician = Person('labour member')
Politician.sayHi()
Politician.howMany()

print ''

gino.sayHi()
gino.howMany()

#############################################################################

# create a bankaccont class

class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

a= BankAccount()

b=BankAccount()
a.deposit(100)
b.deposit(50)
a.withdraw(10)
############################################################################

## example of inheritance
#We see in the example above that the child has overridden the parent’s method1 ,
#causing it to nowrepeat the string seven times.
#The child has inherited the parent’s method2 ,so it can use it without having
#to define it.The child also adds some features to the parent class,
##namely a new variable b and a new method, method3 .


class Parent:
    def __init__(self, a):
        self.a = a
    def method1(self):
        print(self.a*2)
    def method2(self):
        print(self.a+ ' !!! ' )
class Child(Parent):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def method1(self):
        print(self.a*7)
    def method3(self):
        print(self.a + self.b)
p = Parent( ' hi ' )
c = Child( ' hi ' , ' bye ' )
print( ' Parent method 1: ' , p.method1())
print( ' Parent method 2: ' , p.method2())
print()
print( ' Child method 1: ' , c.method1())
print( ' Child method 2: ' , c.method2())
print( ' Child method 3: ' , c.method3())
################################################################

# Create a test class with magic methods( these methods are always available)

class TestClass(object):
        def __init__(self):
                print 'object = TestClass() ran'
        def __getitem__(self,name):
                print 'var = TestClass[%s] ran' % name
                return 0
        def __setitem__(self,name,value):
                print 'TestClass[%s] = %s ran' % (name, value)
        def __call__(self,printwhat):
                print 'TestClass(%s) ran' % printwhat
                print printwhat
 
object = TestClass()
print''
var = object['whatever']
print ''
object['woohoo'] = 0
print ''
object('Hello, World!')



##############################################################################
### Excercises
##############################################################################

# Ex 6_1
#whats the ouput of this script?
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print a.f(), b.f()
print a.g(), b.g()

################################################################################

#Ex6_2

# write a small class about glasses in a restaurant:
