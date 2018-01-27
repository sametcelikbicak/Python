def tambolenleri(sayı):
    tambolenler = []
    for i in range(2, sayı):
        if (sayı % i == 0):
            tambolenler.append(i)
    return tambolenler

while True:
    sayı = input("Sayı:")
    if (sayı == "q"):
        print("programdan çıkılıyor")
        break
    else:
        sayı = int(sayı)
        print("tam bölenler", tambolenleri(sayı))
