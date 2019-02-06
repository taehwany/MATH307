# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 22:27:26 2018

@author: USER
"""
import random as rn;
import numpy as np
import pandas as pd
print ("Welcome to Peter's machine, the Randomizer 3000! There are 3 coins in the machine, a coin that has '1' on both sides, a coin that has '2' on both sides, and a coin that has '1' on one side and '2' on the other. Surface refers to the coin that was chosen and when its front was only seen. Under refers to the number under the coin that was chosen.")
x = 0;
y = 0;
z = 0
two = [2,2]
one = [1,1]
fair = [1,2]
twoFlipped = [2,2]
oneFlipped = [1,1]
fairFlipped = [2,1]
# all possible coins
total = [two, one, fair, twoFlipped, oneFlipped, fairFlipped]
chooseList = []
totalList = []
numberValue = []
# 100 trials
while x < 100:
# choose from the list of lists
    chooseList = rn.choice(total)
# pull out the first value of the list
    numberValue = chooseList[0]
# if it is two coin, count
    if chooseList == two:
        y = y + 1
# if the two coin or the fair coin has a 2, then count
    if numberValue == 2:
        z = z + 1
    totalList.append(chooseList)
    machine = pd.DataFrame(totalList, columns = ['Surface', 'Under'])
    x = x + 1
# check machine
print (machine)
# approximation
print (y/z)
print ("Thank you for using this machine!")


