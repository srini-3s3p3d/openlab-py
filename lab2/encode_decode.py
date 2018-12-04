def encode1(data):
    char=""
    for ch in data:
        ch=chr(ord(ch)+4)
        char+=ch
    return char

def decode(data):
    char=""
    for ch in data:
        ch = chr(ord(ch) - 4)
        char += ch
    return char

input=input('Enter a secret message:  ')
secret=encode1(input)
print('Secret is : '+ secret)
data=decode(secret)
print('The decoded secret is '+ data)

