def sum_array(arr):
    if arr == None or arr == [] or len(arr) == 1:
        return 0
    else:
        return sum(arr) - (min(arr)+max(arr))