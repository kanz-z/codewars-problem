def remove_every_other(my_list):
    arr = []
    odd = 1
    for i in my_list:
        if odd == 1:
            arr.append(i)
            odd -= 1
        else:
            odd += 1
    return arr