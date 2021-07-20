import numpy as numpy
x = random.poisson(lam=2,size=10)
print(x)

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.uniform(size=3000), hist=False)
plt.show()

import numpy as np
x = random.logistic(loc=2,scale=1,size(2,3))
print(x)