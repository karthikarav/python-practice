try:
 y = 30
 print(y)
except:
 print('conformed')

try:
    f = open('file.py')
    f.write('karthika ravi')
except:
    print('something went wrong')
finally:
    f.close()
    
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
