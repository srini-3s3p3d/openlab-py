COMMON=['is','an','the','of','is','from','it','to','be','a','i','me','you','are','where',
        'when','what','how']
f1=open('file1.txt','r')
f2=open('file2.txt','r')
f3=open('common.txt','w+')
c1=f1.read()
c2=f2.read()
c1=c1.split()
c2=c2.split()
# for c in c1:
#         if c not in COMMON:
#                 f3.write(c)
#                 f3.write('\n')
# for c in c2:
#     if c not in COMMON:
#         if c not in f4.read():
#             f3.write(c)
#             f3.write('\n')

for c in c1:
    if c not in COMMON:
        for d in c2:
            if c==d:
                f3.write(c)
                f3.write('\n')
f1.close()
f2.close()
f3.close()