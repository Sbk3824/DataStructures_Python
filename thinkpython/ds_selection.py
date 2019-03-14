import string
import os

print string.punctuation

fout = open('output.txt','w')
print fout

line1 = "This here's the wattle,\n"
fout.write(line1)
line2 = "the emblem of our land.\n"
fout.write(line2)
fout.close()

