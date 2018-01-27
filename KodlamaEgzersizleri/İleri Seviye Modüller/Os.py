import os
from datetime import datetime

#print(dir(os))

#print(os.getcwd())
#os.chdir("/Users/sametcelikbicak/Desktop")
#print(os.getcwd())
#print(os.listdir())

# for i in os.listdir():
#     print(i)

#os.mkdir("Deneme1")
#os.mkdir("Deneme2/Deneme3")#hata veriyor iç içe klasör oluşturma başka fonksiyonla yapılıyor
#os.makedirs("Deneme2/Deneme3")
#os.rmdir("Deneme2/Deneme3")
#os.mkdir("Deneme2/Deneme3")
#os.rmdir("Deneme1")
#os.removedirs("Deneme2/Deneme3")
#os.rename("test.txt","test2.txt")
#os.rename("test2.txt","test.txt")
#print(os.stat("test2.txt"))
#print(os.stat("test2.txt").st_mtime)
#print(datetime.fromtimestamp(os.stat("test2.txt").st_mtime))
# print(os.walk("/Users/sametcelikbicak/Projects/UDEMY/Python"))
# for klasor_yolu,klasor_isimleri,dosya_isimleri in os.walk("/Users/sametcelikbicak/Projects/UDEMY/Python"):
#     print("Klasör Yolu",klasor_yolu)
#     print("Klasör İsimleri", klasor_isimleri)
#     print("Dosya İsimleri", dosya_isimleri)
#     print("*******************************************************")
for klasor_yolu,klasor_isimleri,dosya_isimleri in os.walk("/Users/sametcelikbicak/Projects/UDEMY/Python"):
    for i in dosya_isimleri:
        if (i.endswith(".py")):
            print(i)