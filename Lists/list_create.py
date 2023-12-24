#initializing list
##with list() function
l1=list((1,2,3))
##with [] braces
l2=[3,4,5]
##with list comprehension
l3=list(x for x in range(0,11,2))
#outputs
print("\nlist initialized with list() function-->{}".format(l1))
print("list initialized with [] braces-->{}".format(l2))
print("list initialized with list_comprehension-->{}\n".format(l3))

#lists can be heterogenous and nested
l4=[1,2,(3,4,5),"hello",[1,2,3]]
#output
print("Heterogenous list-->{}".format(l4))
#lists can be accessed with index or loops
for i in l4:
    print("Type of {}-->{}".format(i,type(i)))
    
#nested list/2darray
l5=[
    [1,2,3],
    [4,5,6]
]
print("\nnested list-->{}".format(l5))
print("Accessing a data from nested list-->{}".format(l5[1][2]))

