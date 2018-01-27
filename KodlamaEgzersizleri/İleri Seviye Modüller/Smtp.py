import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

gonderen = input("Gönderen Mail Adresi:")
alici = input("Alıcının Mail Adresi:")
bilgi = input("Bilgi Mail Adresi:")

mesaj = MIMEMultipart()
mesaj["From"] = gonderen
mesaj["Cc"] = bilgi
mesaj["To"] = alici
mesaj["Subject"] = "Python Smtp İle Mail Gönderme"

yazi = """

Python ve PyCharm ile Smtp üzerinden mail gönderimi
Ders içeriğindeki gibi sabit değil kullanıcıdan alınan bilgilere
göre mail gönderimi için düzenlendi.

GitHub:https://github.com/sametcelikbicak/Python/blob/master/KodlamaEgzersizleri/İleri%20Seviye%20Modüller/Smtp.py

Samet ÇELİKBIÇAK

"""

mesaj_govdesi = MIMEText(yazi,"plain")
mesaj.attach(mesaj_govdesi)

try:
    kullanici_adi = input("Kullanıcı Adı:")
    sifre = input("Şifre:")
    mail = smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login(kullanici_adi,sifre)
    mail.sendmail(mesaj["From"],mesaj["To"],mesaj.as_string())
    print("Mail başarılı olarak gönderildi.")
    mail.close()
except:
    sys.stderr.write("Bir sorun oluştu")
    sys.stderr.flush()