cheese = ['Cheddar','Edam', 'Gouda']
num = [17,256]

print 'Edam' in cheese

# Read elements of list
for c in cheese:
	print c

# Write and Update the elements, make use of indices, combine range and len
for i in range(len(cheese)):
	cheese[i] = cheese[i]+'New'
	print cheese[i]

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print c

print [0] * 4
print [1, 2, 3] * 3

t = ['a', 'b', 'c', 'd', 'e', 'f']
print t[1:3]
print t[:4]
print t[3:]
print t[:]
t[1:3] = ['x','y']
print t

print "-------METHODS--------"

t.append('g')
print t

a.extend(b)
print a

t.sort()
print t

print "sum of list a:", sum(a)

print "-------Deleting Elements--------"
x = t.pop(1) #modifies the list and returns the element that was removed
print t
print x

del t[1] 
print t

t.remove('x') # Delete the value
print t

# Lists and Strings

st = 'spam'
print st
ls = list(st)
print ls

stw = "Spam is not spam"
print stw
lsw = stw.split()
print lsw

ss = ['spams','is','not','spam']
delimiter = ' '
print delimiter.join(ss)
print ss 


