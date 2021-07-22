numpy ufuncs:

import numpy as np
x = [1,4,7,8]
y = [5,4,9,2]
z = np.add(x,y)
print(z)

import numpy as np
arr1 = np.array([30,45,56,27])
arr2 = np.array([3,5,8,9])
newarr = np.divide(arr1,arr2)
print(newarr)

import numpy as np
arr1 = np.array([30,45,56,27])
arr2 = np.array([3,5,8,9])
newarr = np.divmod(arr1,arr2)
print(newarr)

import numpy as np
arr = np.array([30,-45,56,-27])
newarr = np.absolute(arr)
print(newarr)

import numpy as np
arr = np.array([-5.2666,5.2666])
newarr = np.trunc(arr)

import numpy as np
arr = np.array([-5.2666,5.2666])
newarr = np.floor(arr)
print(newarr)

import numpy as np
arr = np.array([-5.2666,5.2666])
newarr = np.ceil(arr)
print(newarr)


