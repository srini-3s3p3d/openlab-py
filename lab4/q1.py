import re

sel = 0
data = ''
words = []

def profile():
    choice = int(input('Enter 1 to rewrite your profile or 2 to add information to your existing profile'))
    if (choice == 1):
        pr = open('my_prof.txt', 'w+')
        data = input('Enter contents of your profile...')
        pr.write(data)
        pr.write('\n')
        pr.close()
    elif (choice == 2):
        pr = open('my_prof.txt', 'a+')
        data = input('Enter additional details...')
        pr.write(data)
        pr.write(' ')
        pr.close()
    else:
        print('Wrong choice')


def pali():
    pr = open('my_prof.txt', 'r+')
    pal = open('pali.txt', 'w+')
    data = pr.read()
    words = data.split()
    for x in words:
        l = len(x)
        flag = 0
        for k in range(0, int((l - 1)/2)):
            if (x[k] == x[l-1-k]):
                flag = 0
            else:
                flag=1
        if flag == 0:
            pal.write(x)
            pal.write(' , ')
    print('Written palindromes into file')
    pr.close()
    pal.close()


def even_words():
    pr = open('my_prof.txt', 'r+')
    data = pr.read()
    print('Your profile contents are...')
    print()
    print(data)
    words = data.split(' ')
    print()
    print('Words with even number of charachters are')
    for x in words:
        if len(x) % 2 == 0:
            print(x)
    words.clear()


def sort_file():
    pr = open('my_prof.txt', 'r+')
    srt = open('sort.txt', 'w+')
    data = pr.read()
    print('Your profile contents are...')
    print()
    print(data)
    words = data.split(' ')
    print()
    max = 0
    for x in words:
        if len(x) > max:
            max = len(x)
    # print(max)
    for i in range(max + 1):
        for x in words:
            if len(x) == i:
                srt.write(x)
                srt.write(' , ')
    print('Sort file written')


# creating required files
# a=open('my_prof.txt','x')
# b=open('pali.txt','x')
# c=open('sort.txt','x')

while (1):
    print()
    print('Enter one of the given options')
    print('1 to write/update your profile')
    print('2 to find palindromes in your profile')
    print('3 to print words with even length')
    print('4 to sort the file contents in ascending order of length')
    print('-1 to exit')
    sel = int(input())
    if (sel == -1):
        print('Thank you')
        break
    if (sel == 1):
        profile()
    elif (sel == 2):
        pali()
    elif (sel == 3):
        even_words()
    elif (sel == 4):
        sort_file()
    else:
        print('Invalid choice... Please try again...')
