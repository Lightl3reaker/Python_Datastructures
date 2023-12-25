#created a set
set1={1,2,3}
print("Original set",set1)
#adding element to set
##adding single element
set1.add(5)
print("Added 5 in set",set1)
##adding multiple with update() method
set1.update({4,7})
print("Added multiple with update-->",set1)

#deleting elements
##delete single element
set1.discard(4)#if use remove ,it will show error when elem to delete is not there
print("Removed 4 with discard() method-->",set1)
popper=set1.pop()
print("Poped set-->",set1)
print("Popped item-->",popper)

#Clearing the set
set1.clear()
print("Set is now cleared-->",set1)
