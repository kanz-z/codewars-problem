def series_sum(n):
    sum = 1.00
    for i in range(n-1):
        sum += 1/(4+3*i)
    return str(f"{sum:.2f}") if n > 0 else "0.00"