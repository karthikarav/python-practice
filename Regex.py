Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> str = "How are you. How is everything"
>>> matches = re.search("How", str)
>>> print(matches.span())
(0, 3)
>>> print(matches.group())
How
>>> print(matches.string)
How are you. How is everything
>>> import re
>>> matches = re.search("How", str)
>>> print(type(matches))
<class 're.Match'>
>>> print(matches)
<re.Match object; span=(0, 3), match='How'>
>>> import re
>>> str = "How are you. How is everything"
>>> matches = re.findall("How", str)
>>> matches = re.search("How", str)
>>> matches = re.split("How",str)
>>> print(matches)
['', ' are you. ', ' is everything']
>>> print(matches)
['', ' are you. ', ' is everything']
>>> 