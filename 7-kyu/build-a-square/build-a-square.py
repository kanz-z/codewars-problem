def generate_shape(n):
    return "".join(["+" * n + "\n" if i != n-1 else "+" * n for i in range(n)])