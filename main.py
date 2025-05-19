from linear_sort import *
from binary_search import *
from quick_sort import *

print('Run')
lst1 = [9, 65, 4, 4, 6, 0, 5, 2, 1]
lst2 = lst1.copy()
lst3 = lst1.copy()
lst4 = lst1.copy()
lst5 = lst1.copy()
lst6 = lst1.copy()

print(lst1)
print(selecttion_sort(lst2))
print(buble_sort(lst3))
print(insertion_sort(lst4))
print(quick_sort(lst5))
print(quick_sort(lst6))

print(binary_search(lst2, 2))

