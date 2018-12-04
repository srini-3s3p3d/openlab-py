list1 = ['john', 'tony', 'luck', 'o', 'mIssissippi']

def replace_vowel(mlist):
    vowels = 'aeiou'
    newlist = []
    for word in mlist:
        for char in word:
            if char.lower() in vowels:
                word = word.replace(char, '-')
        newlist.append(word)
    # newlist = [c.replace(vowels, '-') for c in mlist]
    return newlist

print(replace_vowel(list1))