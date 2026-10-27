def first_non_consecutive(arr):
    for i in range(len(arr) - 1):
        if arr[i] + 2 == arr[i+1]:
            return arr[i+1]
    return None