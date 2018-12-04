a=1
b=1
c=1
input=int(input('Enter size of tribonacci series'))
print(a, end =" ")
print(b, end =" ")
print(c, end =" ")
for i in range(0,input-3):
    d=a+b+c
    print(d, end =" ")
    a=b
    b=c
    c=d