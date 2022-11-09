count = 0
with open('user-words.txt', 'w') as f:
    while True:
        word = input('sana: ')
        if word == 'lopeta':
            break
        f.write(word + '\n')
        count += 1

print(f"{count} riviä kirjoitettu tiedostoon!")
