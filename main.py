def teskari_satrlar(satrlar):
    yangi_satrlar = []
    for satr in satrlar:
        sozlar = satr.split()
        yangi_sozlar = [soz[::-1] for soz in sozlar]
        yangi_satr = ' '.join(yangi_sozlar)
        yangi_satrlar.append(yangi_satr)
    return yangi_satrlar

satrlar = ["Hello world", "Python dasturlash", "Teskari satrlar"]
print(teskari_satrlar(satrlar))
