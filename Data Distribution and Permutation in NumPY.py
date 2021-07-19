## Random
from numpy import random
x = random.choice([35,19,20,34,12,11,200], size=(3, 5))
print(x)

## Data Distribution
from numpy import random
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)

## Permutation
from numpy import random
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
a=random.permutation(arr)
print(a)



