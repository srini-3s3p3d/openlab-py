def translate(mode,msg,key):
    if mode[0]=='d':
        key=-key
    translated=''

    for symbol in msg:
        if symbol.isalpha():
            num=ord(symbol)
            num+=key

            if symbol.isupper():
                if num>ord('Z'):
                    num-=26
                elif num<ord('A'):
                    num+=26
            elif symbol.islower():
                if num>ord('z'):
                    num-=26
                elif num<ord('a'):
                    num+=26
            translated+=chr(num)
        else:
            translated+=symbol
    
    return translated

data= translate('e','wxyz',4)
print('Encrypted data is '+data)