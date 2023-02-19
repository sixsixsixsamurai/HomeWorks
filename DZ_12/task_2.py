def to_dict(lst: list):
    take_dict = {}
    for i in lst:
        take_dict[i] = i
    return take_dict

print(to_dict(["oil", "acer", 123, "qwerty"]))
