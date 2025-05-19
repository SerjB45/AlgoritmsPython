def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        left = [i for i in arr[1:] if i <= pivot]
        # middle = [i for i in arr[1:] if i == pivot]
        right = [i for i in arr[1:] if i > pivot]
        
        return quick_sort(left) + [pivot] + quick_sort(right)
    
def quick_sort_2(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [i for i in arr if i <= pivot]
        middle = [i for i in arr if i == pivot]
        right = [i for i in arr if i > pivot]
        
        return quick_sort(left) + middle + quick_sort(right)    