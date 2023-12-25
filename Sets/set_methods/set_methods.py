#Created two sets
s1={1,2,3}
s2={x for x in range(4,7)}
s3={x for x in range(0,9)}
print("Set1",s1)
print("Set2",s2)
print("Set3",s3)

#Following set methods will return a new set
#Union
##using union()
setuni=s1.union(s2)
##using pipe
setuni2=s1|s2
print("Unioned set with pipe operator-->",setuni2)
print("Unioned set-->",setuni)

#Intersection
##intersection()
setinter=s1.intersection(s3)
setinter2=s2.intersection(s3)
##using ampersand
setinter3=s1 & s3
print("Intersected set1 and set3-->",setinter)
print("Intersected set2 and set3-->",setinter2)
print("Intersected with ampersand-->",setinter3)

#Difference
##difference()
diff=s3.difference(s1)
##using minus operator
diff1=s3-s2
print("Differenced set3 and set1-->",diff)
print("Differenced set3 and set2 with minus opt-->",diff1)

#Symmetric Difference
sysdiff=s1.symmetric_difference(s3)
sysdiff1=s2 ^ s3
print("Symmetric differenced 1 and 3-->",sysdiff)
print("Symmetric differenced 2 and 3 using ^ operator-->",sysdiff1)










