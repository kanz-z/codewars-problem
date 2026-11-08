def correct(s):
    return s.translate(str.maketrans({"0": "O", "5": "S", "1": "I"}))