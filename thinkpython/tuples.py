"""
A tuple is a sequence of values. The values can be any type, and they are indexed by
integers, so in that respect tuples are a lot like lists. The important difference is that tuples
are immutable.
"""
t = 'a', 'b', 'c', 'd', 'e'
print t

s = tuple()
print s

st = tuple('lupins')
print st

print t[0]

print t[1:3]

addr = 'monty@python.org'
uname, domain = addr.split('@')

print uname, domain

dm = divmod(7, 3)
print dm

quot, rem = divmod(7, 3)
print quot
print rem

def printall(*args):
	print args

printall(8,10)

# List and Tuples

s = 'abc'
t = [0,1,2]
print zip(s,t)
print zip('Anne', 'Elk')

t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
	print number, letter

"""
Dictionaries and Tuples
Dictionaries have a method called items that returns a list of tuples, where each tuple is a
key-value pair.
"""
d = {'a':0, 'b':1, 'c':2}
t = d.items()
print t

t = [('a', 0), ('c', 2), ('b', 1)]
d = dict(t)
print d

d = dict(zip('abc', range(3)))
print d
