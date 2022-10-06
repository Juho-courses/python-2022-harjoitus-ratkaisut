def kysele():
    ret = {}
    while True:
        syote = input('avain:arvo: ')
        if syote == 'stop':
            break
        syote = syote.split(':')
        ret[syote[0]] = syote[1]
    return ret


d = kysele()
print(d)
