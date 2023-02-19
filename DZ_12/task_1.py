def change(lst: list):
    if len(lst) >= 2:
        a = lst[0]
        lst.reverse()
        b = lst[0]
        lst.reverse()
        lst[0] = b
        lst.reverse()
        lst[0] = a
        lst.reverse()
        return lst


print(change(["hello", "1", "2", "3", "have a good day"]))
