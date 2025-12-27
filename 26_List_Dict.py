#Remove duplicate elements from a list.
days_of_weeks = [60, "tue", 55, "thur", 55, "sat", "tue"]
unique_list = []
for i in days_of_weeks:
    if i not in unique_list:
        unique_list.append(i)
print(f"unique list is : {unique_list}")
print(list(set(days_of_weeks))) #short dont use

#Find the second-largest number in a list.
org_list = [1, 4, 2, 3, 5, 6, 10, 1]
n = len(org_list) #8
for i in range(n):
    for j in range(i + 1, n):
        if org_list[i] < org_list[j]:
            t = org_list[i]
            org_list[i] = org_list[j]
            org_list[j] = t
print( "second-largest number in a list.",org_list[1])

#Merge two lists into one list.
list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 5, 2]
list3 = list2 + list1
print(list3)

#Find common elements between two lists.
list3 = [1, 2, 3, 4]
list4 = [4, 5, 6, 5, 2]

for i in list3:
    for j in list4:
        if i == j:
            print(i, end=",")
            break
print("\n=======")

#Find elements present in first list but not in second.
list4 = [1, 2, 3, 4]
list5 = [4, 5, 6, 5, 2]
for x in list4:
    if x not in list5:
        print(x)

#DICTIONARY LOGIC
#Count frequency of elements in a list using a dictionary.

