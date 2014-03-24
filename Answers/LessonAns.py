for ListName in ['joe','gino','lino','omar','putin','boris','gordon']:
    invite = 'hi there ' + ListName + '.  lets get together for a code session!'
    print(invite)


vowels = "aeiou"
for v in vowels:
  if v in "uranium":
      print v

##  Ex3a

i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
     if not(i%j): break
     j = j + 1
     if (j > i/j) : print i, " is prime"
     i = i + 1
print "Good bye!"

## Ex3c

number = input('enter a non-negative integer to take the factorial of:  ')

product = 1
for i in range(number):
    product = product * (i+1)

print(product)


