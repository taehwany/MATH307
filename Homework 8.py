import numpy as np
import pandas as pd 
import scipy.stats as stats 
theRange = np.arange(0, 100001, 1)
theList = []
# First Row 
theList.append(stats.binom.pmf(np.arange(0, 100001, 1),10,0.3))
# Second Row
theList.append(stats.binom.pmf(np.arange(0, 100001, 1),100,0.03))
# Third Row
theList.append(stats.binom.pmf(np.arange(0, 100001, 1),1000,0.003))
# Fourth Row
theList.append(stats.binom.pmf(np.arange(0, 100001, 1),10000,0.0003))
# Fifth Row
theList.append(stats.binom.pmf(np.arange(0, 100001, 1),100000,0.00003))
# Sixth Row
theList.append(stats.poisson.pmf(np.arange(0, 100001, 1),3))
df = pd.DataFrame(theList)
print (df)