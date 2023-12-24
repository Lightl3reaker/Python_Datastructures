#sorting by length fo string
my_list = ['apple', 'banana', 'kiwi', 'orange']
print(f"Original list-->{my_list}")
my_list.sort(key=lambda x: len(x))
print(f"Sorted with len-->{my_list}")
#sorting by last char of string
my_list1= ['apple','zoo', 'banana', 'kiwi', 'orange','umbrella','bomb','cupboard']
print(f"Original-->{my_list1}")
my_list1.sort(key=lambda x: x[-1])
print(f"Sorted by last character-->{my_list1}")
#sort with number of vowels
def vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')
my_list2=['apple','banana','kiwi','orange']
print(f"Original list->{my_list2}")
my_list2.sort(key=vowels)
print(f"Sorted by number of vowels-->{my_list2}")
#sorting by sum of each nested list
list1=[[1,2,3],[12,3],[3,3,4],[6,7]]
print(f"Original list->{list1}")
list1.sort(key=lambda x: sum(x))
print(f"Sorted by summation->{list1}")