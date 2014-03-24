
# create a dictionary

profile = {'Name':"",'Desc':"", 'Race':"",'Gender':"",'Muscle':0,'Brainz':0,'Speed':0,'Charm':0}

print profile

# access contents of  dictionary using for loop

print ''

for key in  profile:
    print key

# print the keys
print  profile.keys()

print '########################'
# print the values
print profile.values()

#print key-value pairs
print '#########################'
print profile.items()

print sorted(profile.items())

