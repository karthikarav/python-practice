import re
txt = "rain in chennai"
x = re.search("^rain.*chennai!",txt)
if x:
    print('yes,we have atleast one match')
else:
    print('no match')

import re
txt = 'rain in chennai'
x =  re.findall('in',txt)
if x:
    print('yes,we have atleast one match')
else:
    print('no match')

    
import re
txt = 'rain in chennai'
x = re.split('\s',txt)
print(x)

import re
txt = 'rain in chennai'
x = re.sub('/s','5'.txt)
print(x)




