def remove_smallest(numbers):
    min_removed = 0
    arr = []
    for i in numbers:
        if i == min(numbers) and min_removed == 0:
            min_removed += 1
        else:
            arr.append(i)
            
    return arr
        