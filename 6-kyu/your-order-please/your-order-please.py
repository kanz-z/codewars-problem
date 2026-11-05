def order(s):
    if s != '':
        new = []
        sen = s.split(' ')
        number = ["".join([char for char in teks if char.isdigit()]) for teks in sen]
        convertion = [int(num) for num in number]
        sort = sorted(convertion)
        for i in sort:
            for j in convertion:
                if i == j:
                    new.append(sen[convertion.index(j)])
        return " ".join(new)
    return ''