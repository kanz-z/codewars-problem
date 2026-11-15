def number(b):
    person = 0
    for i in b:
        person += i[0]
        person -= i[1]
    return person