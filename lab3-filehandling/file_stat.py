import sys
try:
    #create file
    f = open("demofile.txt","w+")
    print('File created')
    for i in range(10):
        f.write('This is line %d\n'%(i+1))
    f.close()

    #append to file
    f=open("demofile.txt","a+")
    print('Appending to file..')
    for i in range(10):
        f.write('Appending to file line %d\n' %(i+1))
    f.close()

    #reading file
    f=open("demofile.txt","r")
    if(f.mode=='r'):
        contents=f.read()
        print(contents)
        lines=0
        words=0
        chars=0
        wordlist = contents.split(' ')
        words=len(wordlist)
        chars=sum(len(word) for word in wordlist)
        for c in contents:
            if c == '\n':
                lines+=1
        print('Number of lines is ',lines)
        print('Number of words is ', words)
        print('Number of charachters is ', chars)
except IOError as io1:
    print('File error')
    print(io1)
    sys.exit()
finally:
    print('In finally block, exiting gracefully')