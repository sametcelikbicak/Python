import sqlite3

con = sqlite3.connect("kutuphane.db")

cursor = con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik(isim TEXT, yazar TEXT, yayinevi TEXT, sayfa_sayisi INT)")
    con.commit()

def veri_ekle():
    cursor.execute("insert into kitaplik values('istanbul hatırası','ahmet ümit','everest',561)")
    con.commit()

def veri_ekle2(isim,yazar,yayin_evi,sayfa_sayisi):
    cursor.execute("insert into kitaplik values(?,?,?,?)",(isim,yazar,yayin_evi,sayfa_sayisi))
    con.commit()

def verileri_al():
    cursor.execute("select * from kitaplik")
    liste = cursor.fetchall()
    print("Kitaplık Tablosunun Bilgileri")
    for i in liste:
        print(i)

def verileri_al2():
    cursor.execute("select isim,yazar from kitaplik")
    liste = cursor.fetchall()
    print("Kitaplık Tablosunun Bilgileri")
    for i in liste:
        print(i)

def verileri_al3(yayin_evi):
    cursor.execute("select * from kitaplik where yayinevi = ?",(yayin_evi,))
    liste = cursor.fetchall()
    print("Kitaplık Tablosunun Bilgileri")
    for i in liste:
        print(i)

def verileri_guncelle(eski_yayin_evi,yeni_yayin_evi):
    cursor.execute("update kitaplik set yayinevi = ? where yayinevi = ?",(yeni_yayin_evi,eski_yayin_evi))
    con.commit()

def verileri_sil(yazar):
    cursor.execute("delete from kitaplik where yazar = ?",(yazar,))
    con.commit()


    
#tablo_olustur()
#veri_ekle()
#isim = input("İsim:")
#yazar = input("Yazar:")
#yayin_evi = input("Yayın Evi:")
#sayfa_sayisi = int(input("Sayfa Sayısı:"))
#veri_ekle2(isim,yazar,yayin_evi,sayfa_sayisi)
verileri_al()
#verileri_al2()
#verileri_al3("everest")
#verileri_guncelle('everest','doğan kitap')
verileri_sil("tolkien")
verileri_al()

con.close()
