f = open("for_task5.txt", "r")

words = f.read().split()
num_words = len(words)
print(num_words)
f.close()