import pandas as pd
import numpy as np
x = 0
y = 0
theTruth = 0
data = pd.DataFrame([])
while x < 10000:
    newNumber = np.random.uniform(0, 1, 100)
    i = 0
    even = 0
    odd = 0
    while i < 100:
        if i % 2 == 0:
            if newNumber[i] > 1/2:
                even = even + 1
        else:
            if newNumber[i] < 1/2:
                odd = odd + 1
        if even == 50 & odd == 50:
            theTruth = theTruth + 1
        i = i + 1
    allEvents = pd.DataFrame(newNumber)
    allEvents=allEvents.T
    data = data.append(allEvents)
    x = x + 1
print(data)
print (theTruth)
print ("I expected that even if we make 10,000 rows, it would not be enough for the function to happen. In other words, the number would be 0. If we compute (0.5)^50, it would equal 8.8817842e-16, which is a very minute probability. 10,000 is not enough, so for us to get at least one time when the function is true, we would need at least 1.00e17 rows.") 