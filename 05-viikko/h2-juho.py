from typing import List, Tuple


def kysele(maara):
    luvut = []
    for _ in range(maara):
        luku = int(input('luku: '))
        luvut.append(luku)
    return luvut


def prosessoi(luvut):
    s = sum(luvut)
    l = len(luvut)
    avg = s / l
    return (s, l, avg)


maara = int(input('montako lukua syötät: '))
if maara > 0:
    luvut = kysele(maara)
    tulokset = prosessoi(luvut)

    print(f"sum: {tulokset[0]}, len: {tulokset[1]}, avg: {tulokset[2]}")
