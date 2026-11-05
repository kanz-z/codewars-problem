def increment_string(string):
    i = len(string)
    while i > 0 and string[i-1].isdigit():
        i -= 1
    stri = string[:i]
    angka = string[i:]
    if angka == '':
        return stri + '1'
    return stri + str(int(angka) + 1).zfill(len(angka))