import pickle


data = [{"key": "hello", "key1": "hello1"},
        {'key': 'hello2', 'key1': 'hello3'},
        {'key': 'hello4', 'key1': 'hello5'}]


with open('data.pickle.txt', 'wb') as f:
    pickle.dump(data, f)
