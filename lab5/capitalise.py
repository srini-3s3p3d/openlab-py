import os
outfile = open('out1.txt', 'w')
with open('story.txt', 'r') as f:
    for line in f:
        l=line.title()
        outfile.write(l+" ")