f1=open('Append_sentence.txt','w+')
get=''
get = input('Enter a number(enter q to quit)')
while get!='q':
    f1.write(get)
    get = input('Enter a number(enter q to quit)')
print('Thank you')