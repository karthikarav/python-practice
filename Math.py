Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #To print the natural logarithmic of a number:
>>> import math
>>> number=19e-2
>>> print('log(fabs(x), base) is:', math.log(math.fabs(number),10))
log(fabs(x), base) is: -0.7212463990471709
>>> #To print the exponential of a number and return the floating point:
>>> import math
>>> number = 12e-5
>>> print('The given number (x) is :', number)
The given number (x) is : 0.00012
>>> print('e^x (using exp() function) is :', math.exp(number)-1)
e^x (using exp() function) is : 0.00012000720028804146
