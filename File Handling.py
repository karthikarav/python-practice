Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #To Read Files:
>>> f= open("C:\Users\Aishwarya\Desktop\bio.txt", "r")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> for x in f:
	print(x)

	
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    for x in f:
NameError: name 'f' is not defined
>>> f=open("C:\Users\Aishwarya\Desktop\bio.txt","a")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> f.write("I am a student at SRM University")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    f.write("I am a student at SRM University")
NameError: name 'f' is not defined
>>> f.close()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    f.close()
NameError: name 'f' is not defined
>>> f=open("C:\Users\Aishwarya\Desktop\bio.txt"),"r")
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>> print(f.read())
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(f.read())
NameError: name 'f' is not defined
>>> import os
>>> if os.path.exists("C:\Users\Aishwarya\Desktop\bio.txt"):
	
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
>>>   os.remove("C:\Users\Aishwarya\Desktop\bio.text")
  
SyntaxError: unexpected indent
>>> else:
	
SyntaxError: invalid syntax
>>> print("The file does not exist")
The file does not exist
>>> 