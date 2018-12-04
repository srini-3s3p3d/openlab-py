import re
input=input("Enter sentence: ")
ans=re.sub('[aeiou]','*',input)
print(ans)