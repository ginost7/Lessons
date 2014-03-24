# this is Money class with 2 attributes: dollars & cents
# string method produces an o/p using the dollars & cents

class Money(object) :
    def __init__(self) :
    # Set dollars and cents to 0 initially
        self.dollars = 0
        self.cents = 0
    
    def __str__(self) :
        return "$" + str(self.dollars) + "." + str(self.cents)

    def get_dollars(self) :
        return self.dollars
    
    def get_cents(self) :
        return self.cents
    
    def set_dollars(self, d) :
        self.dollars = d
        
    def set_cents(self, c ) :
        self.cents = c


m = Money()

print str(m)

m.set_dollars(10)

m.set_cents(50)

print str(m)
