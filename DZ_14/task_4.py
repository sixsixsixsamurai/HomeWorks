import random
numbers = []
for i in range(100):
    numbers.append("\n" + str(random.randint(0,100)))


with open("random_numbers.txt", "w") as f:
    f.writelines(numbers)