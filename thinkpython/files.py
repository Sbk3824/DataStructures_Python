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

# Filenames and paths

cwd = os.getcwd()
print cwd

print os.listdir(cwd) # returns a list of the files in given directory

# Pickling

import pickle

t1 = [1,2,3]
print t1
s = pickle.dumps(t1)
print s
t2 = pickle.loads(s)
print t2
print t1 == t2
print t1 is t2