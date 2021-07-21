from numpy import random
x = random.exponential(scale=3,size=1000)
print(x)

from numpy import random
x = random.chisquare(df=3,size=1000)
print(x)

from numpy import random
x = random.rayleigh(scale=3,size=1000)
print(x)

from numpy import random
x = random.zipf(a=50,size=2000)
print(x)

