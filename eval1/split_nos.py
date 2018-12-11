data=[]
while 1:
    no = input('Enter a number(enter "end" to exit) : ')
    if no != 'end':
        data.append(int(no))
    else:
        break

print(data)

if len(data)<4:
    print('Insufficient data..')
    exit()

new=[]

for test in data:
    if test%2==0:
        new.insert(0,test)
    else:
        new.insert(len(data)-1,test)

cnt=0
for n in new:
    if n%2==0:
        cnt+=1
    else:
        break

new[0:cnt]=sorted(new[0:cnt])
new[cnt:len(new)]=sorted(new[cnt:len(new)])

for i in range(0,len(new)-2):
    if new[i+1] == new[i]:
        new.remove(new[i+1])
print(new)