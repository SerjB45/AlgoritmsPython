def binary_search(arr, target):
    
    low = 0
    hight = len(arr) - 1
    while low <= hight:
        middle = (low + hight) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            low = middle + 1
        else:
            hight = middle - 1    
        
    return -1

