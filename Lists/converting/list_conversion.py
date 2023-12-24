#string to list conversion
str="Hello MgMg"
print("Original String-->",str)
#using list() function
list1=list(str)
print(f"Converted in to list directly-->{list1}")
#using string.split()
list2=str.split()
print(f"Converted into list using str.split-->{list2}")

#list to string
List=["Hello","User"]
#using seperator directly
str1=' '.join(List)
#using seperator indirectly
seperator=' '
str2=seperator.join(List)
print(f"List to String-->{str1}")
print(f"List to string indirect->{str2}")
