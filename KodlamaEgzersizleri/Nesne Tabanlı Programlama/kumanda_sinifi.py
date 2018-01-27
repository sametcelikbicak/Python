import random
import time

class Kumanda():

    def __init__(self,tv_durum = "Kapalı", tv_sees = 0, kanal_listei = ["Trt"], kanal = "Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_sees
        self.kanal_listesi = kanal_listei
        self.kanal = kanal

    def tv_ac(self):
        if(self.tv_durum == "Açık"):
            print("Televizyon zaten açık..")
        else:
            print("Televizyon Açılıyor..")
            self.tv_durum = "Açık"

    def tv_kapat(self):
        if(self.tv_durum == "Kapalı"):
            print("Televizyon zaten kapalı..")
        else:
            print("Televizyon Kapanıyor..")
            self.tv_durum = "Kapalı"

    def ses_ayarları(self):
        while True:
            cevap = input("Sesi azalt: '<'\nSesi Artır: '>'\nÇıkış: çıkış")

            if(cevap == "<"):
                if(self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses:", self.tv_ses)
            elif(cevap == '>'):
                if(self.tv_ses != 31):
                    self.tv_ses += 1
                    print("Ses:", self.tv_ses)
            else:
                print("Ses güncellendi:", self.tv_ses)
                break

    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor.")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi.")

    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şuanki kanal:",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\nŞuanki Kanal: {}\n".format(self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal)


kumanda = Kumanda()

print("""********************
Televizyon Uygulaması

1.Tv Aç
2.Tv Kapat
3.Ses Ayarları
4.Kanal Ekle
5.Kanal Sayısını Öğrenme
6.Rastgele Kanala Geçme
7.Televizyon Bilgileri

Çıkmak için 'q' ya basınız.
********************""")

while True:
    islem = input("İşlemi Seçiniz:")

    if(islem == "q"):
        print("Program Sonlandırılıyor.")
        break
    elif(islem == "1"):
        kumanda.tv_ac()
    elif(islem == "2"):
        kumanda.tv_kapat()
    elif(islem == "3"):
        kumanda.ses_ayarları()
    elif(islem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin:")
        eklenecek_kanallar = kanal_isimleri.split(",")
        for eklenecekler in eklenecek_kanallar:
            kumanda.kanal_ekle(eklenecekler)
    elif(islem == "5"):
        print("Kanal Sayısı:", len(kumanda.kanal_listesi))
    elif(islem == "6"):
        kumanda.rastgele_kanal()
    elif(islem == "7"):
        print(kumanda)
    else:
        print("Geçersiz İşlem")

