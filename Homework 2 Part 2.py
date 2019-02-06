# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 00:20:30 2018

@author: USER
"""
import random
from collections import Counter
a = 0
approxTotal = 0
# can change a value to change the amount of times this process goes through
while a < 100:
    urnChoice = []
    x = 0
    y = 0
    z = 0  
# create 40 red chips    
    while x < 40:
        urnChoice.insert(0,'R')
        x = x + 1
# create 60 white chips
    while y < 60:
        urnChoice.insert(0,'W')
        y = y + 1
# does 7 choices
    while z < 7:
        issaChoice = random.choice(urnChoice)
# removes the chip from the list
        urnChoice.remove(issaChoice)
# counts how many white chips
        if issaChoice == 'W':
            y = y - 1
# counts how many red chips
        elif issaChoice == 'R':
            x = x - 1
        z = z + 1
# creates possibility of choosing a red chip from the pile
    approx = x/(y+x)
# adds on to the total possibility * number of times the processes
    approxTotal = approx + approxTotal
    a = a + 1
# find the average approximation
total = approxTotal/(a+1)
print (total)
# we can see the possibility is near 0.40

    
     