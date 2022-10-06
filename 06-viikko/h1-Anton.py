kok_luku = input('syötä kokonaisluku: ')
try:
    kok_luku = int(kok_luku)
    print(str(kok_luku) + ' on kokonaisluku')
except:
    print(str(kok_luku) + ' ei ole kokonaisluku')