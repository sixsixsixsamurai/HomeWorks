def sum_range(start: int, end: int):
    if start < end:
        a = start
        result = 0
        result += a
        while a < end:
            a += 1
            result += a
    elif start > end:
        a = end
        result = 0
        result += a
        while a < start:
            a += 1
            result += a
    return result


print(sum_range(15, 20))
