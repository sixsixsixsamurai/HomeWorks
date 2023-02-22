def change(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
        return lst


print(change(["hello", 1, 2, 3, "world"]))