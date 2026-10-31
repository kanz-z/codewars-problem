def rot13(m):
    rot = 13
    hasil = ''
    for i in m:
        code = ord(i)
        if 65 <= code <= 90:
            hasil += chr(65 + (code - 65 + rot) % 26)
        elif 97 <= code <= 122:
            hasil += chr(97 + (code - 97 + rot) % 26)
        else:
            hasil += i
    return hasil