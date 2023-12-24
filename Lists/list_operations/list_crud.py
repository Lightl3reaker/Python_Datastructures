
l1=[1,2,3]
#original list
print("\noriginal list-->{}".format(l1))
#appended list
l1.append(4)
print("appended 4 at the end of list-->{}".format(l1))
l1.append(8)
print("appended 8 at the end of list-->{}".format(l1))
#len of list
print("Length of list==>{}".format(len(l1)))
#deleting an element from end
x=l1.pop()
print("Poped list-->{}".format(l1))
print("Poped element-->{}".format(x))
#inserting element
l1.insert(4,7)
print("Inserted 7 at index4 ==>{}".format(l1))
#removing element
l1.remove(3)
print("Removed 3 from list-->{}".format(l1))
#reversing list
l1.reverse()
print("reversed list-->{}".format(l1))
#created a new list of ints
l2=list(i for i in range(0,12))
print("A new list-->{}".format(l2))

#deleting even ints
del l2[0:12:2]
print("Removed even nums==>{}".format(l2))
#copying list
l3=l2.copy()
print("Shallow copy of l2 to l3-->{}".format(l3))
#populating l3 with elements
l3 *= 3
print("Updated l3's elements 3 times-->{}".format(l3))
#removing all elements
l3.clear()
print("Cleared elements from l3-->{}".format(l3))