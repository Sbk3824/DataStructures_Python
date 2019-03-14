
l = [1,2,3,4]
e = [7,8,9]

print "List:",l

print "length:", l.__len__()

print "Mul:", l.__mul__(2)

print "Size", l.__sizeof__()

l.append(5)

print "list:",l

print "count of 5 in list :", l.count(5)

l.insert(1,5)

print "list:",l

l.reverse()
print "Reversed List:", l

l.sort()
print "Sorted:", l

print "Representation:", l.__repr__()

l.extend(e)
print "Extended List:", l

l.remove(5) # removes first occurence of 5
print "New List:", l
