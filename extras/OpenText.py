# this script opens a txt file, IT AS TO BE IN THE SAME DIRECTORY

import os
file = open("super_villains.txt")
for line in file:
    line = line.strip()
    print(line)
    #file.close() 
