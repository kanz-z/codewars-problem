def dig_pow(n, p):
    angka = 0
    string = str(n)
    for i in string:
        angka += int(i) ** p
        p += 1
    return angka // n if angka % n == 0 else -1