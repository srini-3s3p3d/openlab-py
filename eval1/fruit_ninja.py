FRUIT_NAMES = ['apple', 'banana', 'orange']
print(FRUIT_NAMES)
fruits1 = []
fruit = ''
new = []

def cut_fruits(fruits):
    for test in fruits:
        if test in FRUIT_NAMES:
            n = len(test)
            va = ''
            if n % 2 == 0:
                for i in range(0, int(n / 2)):
                    va += test[i]
                new.append(va)
                va = ''
                for i in range(int(n / 2), n):
                    va += test[i]
                new.append(va)
            else:
                for i in range(0, int(n / 2 + 0.5)):
                    va += test[i]
                new.append(va)
                va = ''
                for i in range(int((n / 2) + 0.5), n):
                    va += test[i]
                new.append(va)

        if test not in FRUIT_NAMES:
            new.append(test)

        print('In loop: ', new)
        print(fruits)

while 1:
    fruit = input('Enter a fruit(enter "end" to exit)')
    if fruit != 'end':
        fruits1.append(fruit)
    else:
        break

print(fruits1)

cut_fruits(fruits1)

print()
print(new)