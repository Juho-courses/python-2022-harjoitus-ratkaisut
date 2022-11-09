import random


def generoi_lottorivi():
    # luodaan lista mahdollisista numeroista
    v = list(range(1, 41))
    # valitaan 7 uniikkia numeroa
    row = random.sample(v, 7)
    return row


def rivi_ok(row):
    r = set(row)

    # set-muutos jättää jäljelle vain uniikit arvot.
    # jos pituus muuttuu, tiedetään että kaikki ei ollut uniikkeja.
    # Samalla tarkastetaan myös numeroiden oikea määrä
    if len(r) != 7:
        return False

    # Tarkastetaan että arvot ovat sallitun rangen sisällä
    if min(r) < 1 or max(r) > 40:
        return False

    # ei osuttu ongelmiin, kaikki hyvin
    return True


# lyhyt
viallinen_rivi = [2, 3, 4, 5, 6, 7]
print(f"rivi {viallinen_rivi}: {rivi_ok(viallinen_rivi)} ")

# liian iso numoro
viallinen_rivi = [2, 3, 4, 5, 6, 7, 41]
print(f"rivi {viallinen_rivi}: {rivi_ok(viallinen_rivi)} ")

# liian pieni numero
viallinen_rivi = [2, 3, 4, 5, 6, 7, 0]
print(f"rivi {viallinen_rivi}: {rivi_ok(viallinen_rivi)} ")

# kaikki ei uniikkeja
viallinen_rivi = [2, 3, 4, 5, 6, 7, 7]
print(f"rivi {viallinen_rivi}: {rivi_ok(viallinen_rivi)} ")

print("")

for _ in range(10):
    r = generoi_lottorivi()
    if rivi_ok(r):
        print(r)
    else:
        print(f"viallinen rivi: {r}")
