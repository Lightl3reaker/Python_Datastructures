#Creating Dictionaries
emptdict={}
dict1={"male":32,"female":40,"young":12,"old":13}
dict2={"name":"Mg Mg","Gender":"Male","Age":23,"Salary per hour":23.33}
dict3={x:x**2 for x in range(11)}
print("Empty dictionary",emptdict)
print("--Dictionary1--")
for x in dict1.keys():
    print(f"{x} : {dict1.get(x)}")
print("--Dictionary2--")
_=[print(f"{x}:{dict2.get(x)}") for x in dict2.keys()]
print("--Dictionary3--")
_=[print(key,dict3[key]) for key in  dict3.keys()]
