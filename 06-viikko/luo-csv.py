import random

first_names = ['Mary', 'Joe', 'Matt', 'Gary', 'Hanna',
               'Jenny', 'Sarah', 'Ash', 'Tina', 'Rose']

last_names = ['Smith', 'Garrison', 'Ketchum', 'Rogers',
              'Johnson', 'Hammett', 'Mercury', 'Goodman']

names = []

names = [f"{fn} {ln}" for fn in first_names for ln in last_names]

random.shuffle(names)

data = [f"{n},{random.randint(20,79)}" for n in names]

for d in data:
    print(d)

with open('data.csv', 'w') as f:
    f.write('name,age\n')
    f.writelines([f"{d}\n" for d in data])
