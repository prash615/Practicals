# Sets are non-sequential collection of items
# comma separated elements enclosed within {b
# sets do not allow duplicate elements
from enum import unique

set1 = {10,"Python", 2.5}
print(set1)
print (type(set1))
# Cannot have indexing with sets

nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = set(nums)
unq_nums = list(set(nums))
print(unq_nums)

