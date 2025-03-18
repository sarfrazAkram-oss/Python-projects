def binary_search_recursive(arr, left, right, target):
    if left > right:
        return -1 
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, left, mid - 1, target)
    else:
        return binary_search_recursive(arr, mid + 1, right, target)

arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
target = 13
result = binary_search_recursive(arr, 0, len(arr) - 1, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")
