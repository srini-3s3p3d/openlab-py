import re
isbn=int(input('Enter a 10 digit ISBN number'))
dts=[]
val=0
while isbn>0:
    dts.append(isbn%10)
    isbn=int(isbn/10)
dts.reverse()
print(dts)
for i in range(0,10):
    print(dts[i])
for i in range(0,10):
    val=val+((i+1)*dts[i])

print(val)
if val%11==0:
    print('It is a valid ISBN number')
else:
    print('It is not a valid ISBN number')