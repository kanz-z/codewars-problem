def stray(arr):
    new = sorted(arr)
    for i in sorted(arr):
        if new[0] == new[1]:
            return new[-1]
    return new[0]