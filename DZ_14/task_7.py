import collections

c = collections.Counter()

f = open("for_task7.txt", "r", encoding="utf-8")

for i in f.read().split():
    c[i] += 1

f.close()
print(c)