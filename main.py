from linear_sort import *
from binary_search import *
# import copy

print('Run')
lst1 = [9, 65, 4, 4, 6, 0, 5, 2, 1]
lst2 = lst1.copy()
lst3 = lst1.copy()
lst4 = lst1.copy()

print(lst1)

selecttion_sort(lst2)
print(lst2)

buble_sort(lst3)
print(lst3)

insertion_sort(lst4)
print(lst4)

print(binary_search(lst2, 2))