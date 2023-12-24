#list1
l1=list((1,2,3,4,5))
print("Original list->{}".format(l1))
#list sclising
print("Sliced from index 0 to 2->{}".format(l1[0:2]))
###List Methods
#max of list
print("Max of list->{}".format(max(l1)))
#min of list
print("Min of list->{}".format(min(l1)))
#adding multiple elements in list
l2=list(x for x in range(5,8))
l1.extend(l2)
print("Updated list-->{}".format(l1))
#searching how many 5 in list
c=l1.count(5)
print(f"Occurence of 5 in list : {c}")
#seraching with index
i=l1.index(5,1,5)
print(f"Index of 5 in first part of list {i}")
#searching with parts of list
i2=l1.index(5,5,7)
print(f"Index of 5 in second part of list {i2}")

