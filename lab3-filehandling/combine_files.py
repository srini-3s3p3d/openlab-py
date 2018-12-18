import sys
try:
    f1=open("file1.txt","r")
    f2=open("file2.txt","r")
    f3=open("file3.txt","w+")
    c1=f1.read()
    c2=f2.read()
    c3=c1+"\n"+c2
    f3.write(c3)
except IOError as io:
    print('error',io)
finally:
    print('In finally block')