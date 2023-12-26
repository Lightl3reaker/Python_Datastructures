#Creating a dictionay
profile={"Name":"Mary","Age":23,"Job":"None"}
print(f"Original Profile")
_=[print(key,profile[key]) for key in profile.keys()]
#Added address,School,Favourite
profile["Address"]="NewYork"
profile["School"]="Harvet"
profile["Favourite"]="Listening Music"
print("\nAdded items in Profile")
_=[print(key,profile[key]) for key in profile.keys()]
#Updated Age
profile["Age"]=30
print("\nUpdated Profile")
_=[print(key,profile[key]) for key in profile.keys()]
#Deleting
del profile["Favourite"]
profile.pop("School")
last_pair=profile.popitem()
print("\nDeleted Favourite,School and last pair")
print("Last pair-->",last_pair)
for key,value in profile.items():
    print(key,value)
#checking key value pair
if "Name" in profile:
    print("\nName exits.")
if "School" not in profile:
    print("\nSchool doesn't exit.")
print("\nCloned dictionay.")
clonedict=profile.copy()
for key,value in clonedict.items():
    print(key,value)
