from kutuphane import *

print("""********************
Kütüphane Programı

1.Kitapları Göster
2.Kitap Sorgulama
3.Kitap Ekle
4.Kitap Sil
5.Baskı Yükselt

Çıkmak için 'q' ya basınız
********************""")

kutuphane = Kutuphane()

while True:
    islem = input("Yapacağınız İşlem:")

    if (islem == "q"):
        print("Program sonlandırılıyor")
        break
    elif (islem == "1"):
        kutuphane.kitaplari_goster()
    elif (islem == "2"):
        isim = input("Görmek İstediğiniz Kitap Adı:")
        print("Kitap sorgulanıyor")
        time.sleep(2)
        kutuphane.kitap_sorgula(isim)
    elif (islem == "3"):
        isim = input("Kitap Adı:")
        yazar = input("Yazar:")
        yayinevi = input("Yayınevi:")
        tur = input("Tür:")
        baski = int(input("Baskı:"))
        yeni_kitap = Kitap(isim,yazar,yayinevi,tur,baski)
        print("Kitap ekleniyor")
        time.sleep(2)
        kutuphane.kitap_ekle(yeni_kitap)
        print("kitap eklendi.")
    elif (islem == "4"):
        isim = input("Sileceğiniz Kitap Adı:")
        cevap = input("Emin misiniz ? (E/H)")
        if(cevap == "E"):
            print("kitap siliniyor")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("kitap silindi")
    elif (islem == "5"):
        isim = input("hangi kitabın baskınısı yükseltmek istiyorsunuz ?")
        print("baskı yükseltiliyor")
        time.sleep(2)
        kutuphane.baski_yukselt(isim)
        print("baskı yükseltildi")
    else:
        print("Geçersiz işlem")
