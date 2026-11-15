def sort_by_length(arr):
    result = []
    convert = [len(i) for i in arr]
    while convert:
        minimum = min(convert)
        index = convert.index(minimum)
        result.append(arr[index])
        convert.pop(index)
        arr.pop(index)
    return result