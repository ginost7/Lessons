# Change the numbers of cars, people, and buses and
# trace through each if-statement to see what will be printed

people = raw_input("enter num of people: ") 
cars = raw_input("enter num of cars: ")
buses = raw_input("enter num of buses: ")


if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
