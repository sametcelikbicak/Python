import smtplib
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()
mesaj["From"] = "sametcelikbicak@gmail.com"
mesaj["Cc"] = "sametcelikbicak@gmail.com"
mesaj["To"] = "coskun.m.murat@gmail.com"
mesaj["Subject"] = "Python Smtp İle Mail Gönderme"

yazi = """

Python ve PyCharm ile Smtp üzerinden mail gönderimi

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