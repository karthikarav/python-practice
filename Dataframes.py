Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Panda Dataframe:
>>> import pandas as pd
>>> df= pd.read_csv('C:\Users\Aishwarya\Desktop\data.csv')
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> print(df)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(df)
NameError: name 'df' is not defined
>>> 