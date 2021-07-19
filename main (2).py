import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0, 1, 2, 3, 4, 5])
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot([0,1,2,3,4,5]), hist = False)
plt.show()

from numpy import random
x = random.normal(size=(3,6))
print(x)

from numpy import random
x = random.binomial(n=10,p=0.3,size=200)
print(x)