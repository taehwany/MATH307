# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 18:18:11 2018

@author: USER
"""

import random
from collections import Counter
print ("Welcome to Peter's Machine of URN, which finds the probability of three possibilities: a, b, and c!" )
choice = input("Please choose an option: ")
if choice == "a":     
    approxTotal = 0
    urnChoice = []
    w = 0
    x = 0
    y = 0
    z = 0  
    probabilityA = 1
    probabilityB = 0
    probabilityC = 0
    totalBalls = 35
    # create 40 red balls    
    while x < 13:
        urnChoice.insert(0,'R')
        x = x + 1
    # create 60 white balls
    while y < 10:
        urnChoice.insert(0,'W')
        y = y + 1
    # create 12 blue balls
    while w < 12: 
        urnChoice.insert(0,'B')
        w = w + 1
    # does 7 choices
    while z < 7:
        issaChoice = 'W'
    # counts how many white balls
        if issaChoice == 'W':
            totalA = (y/totalBalls)
            totalBalls = totalBalls - 1
            y = y - 1
        probabilityA = probabilityA*totalA
        z = z + 1
    print (probabilityA)
if choice == "b":     
    approxTotal = 0
    urnChoice = []
    w = 0
    x = 0
    y = 0
    z = 0  
    probabilityA = 1
    probabilityB = 1
    probabilityC = 1
    totalBalls = 35
    # create 40 red balls    
    while x < 13:
        urnChoice.insert(0,'R')
        x = x + 1
    # create 60 white balls
    while y < 10:
        urnChoice.insert(0,'W')
        y = y + 1
    # create 12 blue balls
    while w < 12: 
        urnChoice.insert(0,'B')
        w = w + 1
    # does 7 choices
    while z < 4:
        issaChoice = 'W'
        if issaChoice == 'W':
            totalA = (y/totalBalls)
            totalBalls = totalBalls - 1
            y = y - 1
        probabilityA = probabilityA*totalA
        z = z + 1
    z = 0
    while z < 1:
        issaChoice = 'R'
        if issaChoice == 'R':
            totalB = (x/totalBalls)
            totalBalls = totalBalls - 1
            x = x - 1
        z = z + 1
        probabilityB = probabilityB*totalB
    z = 0
    while z < 2:
        issaChoice = 'B'
        if issaChoice == 'B':
            totalC = (w/totalBalls)
            totalBalls = totalBalls - 1
            w = w - 1
        probabilityC = probabilityC*totalC
        z = z + 1
    totalProbability = probabilityC * probabilityB * probabilityA
    print (totalProbability) 
if choice == "c":     
    approxTotal = 0
    urnChoice = []
    w = 0
    x = 0
    y = 0
    z = 0  
    probabilityA = 1
    probabilityB = 1
    probabilityC = 1
    totalBalls = 35
    # create 40 red balls    
    while x < 13:
        urnChoice.insert(0,'R')
        x = x + 1
    # create 60 white balls
    while y < 10:
        urnChoice.insert(0,'W')
        y = y + 1
    # create 12 blue balls
    while w < 12: 
        urnChoice.insert(0,'B')
        w = w + 1
    while z < 5:
        issaChoice = 'B'
        if issaChoice == 'B':
            totalC = (w/totalBalls)
            totalBalls = totalBalls - 1
            w = w - 1
        probabilityC = probabilityC*totalC
        z = z + 1
    while z < 2:
        issaChoice = random.choice(urnChoice)
# removes the chip from the list
        urnChoice.remove(issaChoice)
# counts how many white chips
        if issaChoice == 'W':
            totalA = (y/totalBalls)
            totalBalls = totalBalls - 1
            y = y - 1
        probabilityA = probabilityA*totalA
# counts how many red chips
        if issaChoice == 'R':
            totalB = (x/totalBalls)
            totalBalls = totalBalls - 1
            x = x - 1
        probabilityB = probabilityB*totalB
        if issaChoice == 'B':
            continue
        z = z + 1
    totalProbability = probabilityC * probabilityB * probabilityA
    print (totalProbability) 