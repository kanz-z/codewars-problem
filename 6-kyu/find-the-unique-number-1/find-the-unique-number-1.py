def find_uniq(xs):
    return max(xs) if sorted(xs)[0] == sorted(xs)[1] else sorted(xs)[0]