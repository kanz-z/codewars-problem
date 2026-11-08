def number(lines):
    arr = []
    for i, str in enumerate(lines, start=1):
        arr.append(f"{i}: {str}")
    return arr