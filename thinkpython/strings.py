#Strings are immutable

fruit = 'banana'
letter = fruit[1]

print fruit
print len(fruit)
print letter
print fruit[len(fruit)-1]
print fruit[-1]
print fruit[-2]

print "---------------"

for char in fruit:
	print char

print "---------------"


prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
	print letter + suffix


s = 'Monty Python'
print s[0:5]
print s[6:12]
print fruit[:3]
print fruit[3:]
print fruit[3:3]

print fruit.upper()
print fruit.find('a')
print fruit.find('na')

# in operator

value = 'a' in 'banana'
print 'Value:',value

