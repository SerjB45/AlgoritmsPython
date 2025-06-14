from linear_sort import *
from binary_search import *
from quick_sort import *
from merge_sort import *
from dijkstra import *
from bellman_ford import *
from greedy import *
from knn_algorithm import *
from quick_merge import *

print('Run')
lst1 = [9, 65, 4, 4, 6, 0, 5, 2, 1]
lst2 = lst1.copy()
lst3 = lst1.copy()
lst4 = lst1.copy()
lst5 = lst1.copy()
lst6 = lst1.copy()
lst7 = lst1.copy()

print(lst1)
print(selecttion_sort(lst2))
print(buble_sort(lst3))
print(insertion_sort(lst4))
print(quick_sort(lst5))
print(quick_sort_2(lst6))
print(merge_sort(lst7))

print(binary_search(lst2, 2))

test_dijkstra()
test_bellman_ford()
test_greedy_knapsack()
test_interval_scheduling()
test_nearest_neighbor_tsp()
test_knn_classify()

list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
print( quick_merge(list1, list2))
