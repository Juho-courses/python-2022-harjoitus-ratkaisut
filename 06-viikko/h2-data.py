import sys
data = []

try:
    with open('data.csv', 'r') as f:
        counter = 0
        for line in f:
            if counter == 0:
                counter += 1
                continue
            line = line.strip()
            # print(line)
            d = line.split(',')
            d[1] = int(d[1])
            # print(d)
            data.append(tuple(d))
except FileNotFoundError as e:
    print(f'tiedostoa {e.filename} ei löytynyt')
    sys.exit(1)


###
# Selvitetään alimmat ja ylimmät esiintyvät iät
###
# tapa 1
# min_age = data[0][1]
# max_age = data[0][1]
# for d in data:
#     print(d)
#     if d[1] > max_age:
#         max_age = d[1]

#     if d[1] < min_age:
#         min_age = d[1]
# print(min_age, max_age)

# tapa 2
ages = [d[1] for d in data]
min_age = min(ages)
max_age = max(ages)
print(min_age, max_age)


###
# Etsitään nuorimmat ja vanhimmat henkilöt
###
youngest = [d for d in data if d[1] == min_age]
print(youngest)
oldest = [d for d in data if d[1] == max_age]
print(oldest)

###
# Selvitetään ja tulostetaan jokaisen Matt yhteenlaskettu ikä
###

total = sum([d[1] for d in data if 'Matt' in d[0]])
print(f"Matt's age sum: {total}")
