import random
lottorivi = []
def lotto():
    for _ in range(7):
        lottorivi.append(random.randint(1, 40))
    return lottorivi

def tarkistus(x):
    try:
        x = set(x)
        len(x) == 7
        max(x) < 41
        min(x) > 0
    except:
        print(f"{x} ei ole laillinen lottorivi")
    return (f"{x} on laillinen lottorivi")


print(tarkistus(lotto()))