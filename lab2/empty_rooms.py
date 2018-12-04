input=input('Enter room status')
rooms=list(input)
empty='O'
if(empty not in rooms):
    print('None available')
else:
    print(rooms.index('O'))