f1=open('odd.txt','w+')
f2=open('even.txt','w+')
get=''
get = input('Enter a number(enter q to quit)')
while get!='q':
    get=int(get)
    if get%2==0:
        f2.write(str(get))
    else:
        f1.write(str(get))
    get = input('Enter a number(enter q to quit)')

f1.close()
f2.close()
print('Thank you')