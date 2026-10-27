def get_count(sentence):
    return sum([1 if i in 'aiueo' else 0 for i in sentence])