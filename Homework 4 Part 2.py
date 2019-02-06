#A)
import random as rn
import pandas as pd
x = 0
y = 1
z = 1
theY = []
theNewY = []
newY = 0.0
while y < 101:
    theY = []
    newY = ((0.3)** y)*((0.7)**(100-y));
    theY.append(y)
    theY.append(newY)
    theNewY.append(theY)
    y = y + 1
machine = pd.DataFrame(theNewY, columns = ["Heads", "Probability"])
print(machine)
#B)
machine2 = machine.cumsum()
print(machine2)
#C)
    #A)
y = 1
totalY = 0
totalNewY = 0
finalY = 0
while y < 90:
    newY = ((0.3)** y)*((0.7)**(100-y));
    totalY = totalY + newY;
    y = y + 1
y = 1
while y < 22:
    newY = ((0.3)** y)*((0.7)**(100-y));
    totalNewY = totalNewY + newY;
    y = y + 1
finalY = totalY - totalNewY
print(finalY)
    #B)
#From the pd.DataFrame I got 2.425857e-16 for 89 heads, while for 22 heads I got 0.242586e-16. What we can tell
# is that the answer will be minutely very small, thus the answer we got from 3A) is probably correct!