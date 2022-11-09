try:
    arvo = int(input('kokonaisluku: '))
    print(arvo * arvo)
except ValueError:
    print('syötetty arvo ei ollut kokonaisluku')
