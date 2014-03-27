# ex

# an
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

#################################################################

#ex6_2

class Glass(object):
       def __init__(self, size):
           assert size > 0
           self._size = float(size)  # an attribute
           self._content = float(0.0)  # another attribute
       def __repr__(self):
           if self._content == 0.0:
               return "An empty glass of size %s"%(self._size)
           else:
               return "A glass of size %s cl containing %s cl of water"%(
                       self._size, self._content)
       def fill(self):
           self._content = self._size
       def empty(self):
           self._content = float(0.0)


myGlass = Glass(10)
myGlass
myGlass.fill(); myGlass
myGlass.fill(); myGlass

#################################################################

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
var = object['whatever']
object['woohoo'] = 0
object('Hello, World!')
















       
