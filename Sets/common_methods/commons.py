#Created a set
s={1,2,3}
print("Set--->",s)
print("Length of set",len(s))
for i in range(1,5):
    print(f"{i} in set->",i in s)
x=5
print(f"5 not in set-->{x not in s}")
s1=s.copy()
print("Copy of set/newset-->",s1)
