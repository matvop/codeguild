from collections import Counter

names_to_ages = {
    "Alyssa": 22,
    "Charley": 25,
    "Dan": 25,
    "Jeff": 20,
    "Kasey": 20,
    "Kim": 20,
    "Morgan": 25,
    "Ryan": 25,
    "Stef": 22
}

print(Counter(list(names_to_ages.values())).most_common()[-1][0])
