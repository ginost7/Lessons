
# for loop
print range(1,7)

for i in range(1,7):
    print i

print  ''

# for loop starting at 3 to 
for v in range(5,1,-1):
    print v

print ''    
#create a sequence of 36/2=18 values from 1 to just before 36 stepping by 2
print  range(1,36,2)

for o in range(1,36,2):
    print o

#nest for loop The print statement will be executed 36 times.
print ''
for d1 in range(6):
    for d2 in range(6):
        print d1+1,d2+1,'=',d1+d2+2

# some of Python's objects that can be used with a for loop:
print '###############'

for element in range(1,4): # range
    print element

print '################'

for element in [1, 2, 3]: # list
    print element
    
print '#################'

for key in {'one':1, 'two':2}: # dictionary
    print key
