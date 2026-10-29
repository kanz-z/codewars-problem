def tribonacci(signature, n):
    arr = []
    for i in range(n):
        if i < 3:
            arr.append(signature[i])
        else:
            arr.append(sum(arr[-3:]))
    return arr[:n]
    
        