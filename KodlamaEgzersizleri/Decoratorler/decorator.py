def ekstra(fonk):
    def wrapper(sayilar):
        ciftler_toplami = 0
        cift_sayilar = 0
        tekler_toplami = 0
        tek_sayilar = 0

        for sayi in sayilar:
            if(sayi % 2 == 0):
                ciftler_toplami += sayi
                cift_sayilar += 1
            else:
                tekler_toplami += sayi
                tek_sayilar += 1
        print("Teklerin ortalaması:",tekler_toplami / tek_sayilar)
        print("Çiftlerin ortalaması:",ciftler_toplami / cift_sayilar)
        fonk(sayilar)
    return wrapper


@ekstra
def ortalama_bul(sayilar):
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    print("Genel ortalama:",toplam / len(sayilar))


ortalama_bul([1,2,3,4,34,60,63,32,100,105])
