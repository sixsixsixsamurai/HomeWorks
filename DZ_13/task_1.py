def cache_decorator(func):
    cache_triangle = {}
    cache_circle = {}

    if func.__name__ == "triangle_area":
        def cache_dict(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))

            if key not in cache_triangle:
                cache_triangle[key] = func(*args, **kwargs)

            return cache_triangle[key]

        return cache_dict


    if func.__name__ == "circle_area":
        def cache_dict(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))

            if key not in cache_circle:
                cache_circle[key] = func(*args, **kwargs)

            return cache_circle[key]

        return cache_dict


@cache_decorator
def triangle_area(a: float, b: float) -> float:
    print(f'Вызвана функция triangle_area с аргументами {a} и {b}')
    return a * b


@cache_decorator
def circle_area(r: float) -> float:
    print(f'Вызвана функция circle_area с аргументом {r}')
    return 3.14 * (r * r)


print('Результат выполнения triangle_area(5, 10):', triangle_area(5, 10))
print('Результат выполнения triangle_area(5, 10):', triangle_area(5, 10))
print('Результат выполнения circle_area(20):', circle_area(20))
print('Результат выполнения triangle_area(10, 10):', triangle_area(10, 10))
print('Результат выполнения circle_area(20):', circle_area(20))
