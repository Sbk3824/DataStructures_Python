"""
A dictionary is like a list, but more general. In a list, the indices have to be integers; in a
dictionary they can be (almost) any type.

You can think of a dictionary as a mapping between a set of indices (which are called keys)
and a set of values. Each key maps to a value. The association of a key and a value is called
a key-value pair or sometimes an item.
"""

eng2sp = dict()
print eng2sp # empty dictionary {}

eng2sp['one'] = 'uno'
print eng2sp

eng2sp = {'one':'uno', 'two':'dos', 'three':'tres'}
print eng2sp

print eng2sp['two']

#print eng2sp['four'] 

print len(eng2sp)

print 'one' in eng2sp #True
print 'uno' in eng2sp #False

"""
To see whether something appears as a value in a dictionary, you can use the method
values, which returns the values as a list, and then use the in operator:
"""

vals = eng2sp.values()
print 'uno' in vals #True









