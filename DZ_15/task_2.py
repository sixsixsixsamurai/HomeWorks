import json

a = {"key": 1, "key2": True}
b = {"key": "Hello", "key2": False}

c = {}
for key, value in a.items():
    if key in b:
        c[key] = [value, b[key]]
    else:
        c[key] = value

for key, value in b.items():
    if key not in a:
        c[key] = value

with open('result.json', 'w') as f:
    json.dump(c, f)
