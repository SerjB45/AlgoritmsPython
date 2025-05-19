
def selecttion_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1,n):
            if arr[j] < arr[min_index]:
                min_index = j
            
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr    
    

def buble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr    

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        value = arr[i]
        j = i - 1        
        
        while j >= 0 and value < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = value    
    return arr    
        