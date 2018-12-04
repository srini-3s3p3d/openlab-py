input=input('Enter a word:  ')
ch=""
for i in range(0,len(input)):
    ch+=input[i].capitalize()+(input[i] * (i))+'-'

print(ch)