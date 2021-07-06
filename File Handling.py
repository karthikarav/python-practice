Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #To Read Files:
>>> f= open("C:\Users\Aishwarya\Desktop\bio.txt", "r")
>>> for x in f:
	print(x)
>>> f=open("C:\Users\Aishwarya\Desktop\bio.txt","a")
>>> f.write("I am a student at SRM University")
>>> f.close()
>>> f=open("C:\Users\Aishwarya\Desktop\bio.txt"),"r")
>>> print(f.read())
>>> import os
>>> if os.path.exists("C:\Users\Aishwarya\Desktop\bio.txt"):
>>>   os.remove("C:\Users\Aishwarya\Desktop\bio.text")
>>> else:
>>> print("The file does not exist")

