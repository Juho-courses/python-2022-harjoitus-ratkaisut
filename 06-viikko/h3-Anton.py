sanat = []
n = 1
while True:
    sana = input(f'syötä sana {n}: ')
    if sana == 'lopeta':
        break
    sanat.append(sana)
    n = n + 1
with open('sanat.csv', 'w') as f:
    for d in sanat:
        f.writelines(d + '/n')
print(f"{n - 1} riviä kirjoitettu tiedostoon")