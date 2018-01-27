print("""*****************************
Hesap Makinesi Programı

İşlemler;

1. Toplama İşlemi
2. Çıkarma İşlemi
3. Çarpma İşlemi
4. Bölme İşlemi
*****************************
""")

a = int(input("Birinci Sayı:"))
b = int(input("İkinci Sayı:"))
işlem = input("İşlemi Giriniz:")

if  işlem == "1":
    print("{} ile {} in toplamı {} dir".format(a, b ,a + b))
elif  işlem == "2":
    print("{} ile {} in farkı {} dir".format(a, b ,a - b))
elif  işlem == "3":
    print("{} ile {} in çarpımı {} dir".format(a, b ,a * b))
elif  işlem == "4":
    print("{} ile {} in bölümü {} dir".format(a, b ,a / b))
else:
    print("Geçersiz İşlem...")
