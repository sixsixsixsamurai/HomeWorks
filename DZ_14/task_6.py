with open("for_task6.txt", "r") as f:
    numbers_string = f.read()

numbers = [int(x) for x in numbers_string.split()]
print(numbers)
print(sum(numbers))