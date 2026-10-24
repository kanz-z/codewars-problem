def tower_builder(n):
    arr = []
    for i in range(1, n + 1):
        spasi = " " * (n - i)
        bintang = "*" * (2 * i - 1)
        arr.append(spasi + bintang + spasi)
    return arr
    