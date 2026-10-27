def sum_mix(arr):
    return sum(i if type(i) == 'int' else int(i) for i in arr)