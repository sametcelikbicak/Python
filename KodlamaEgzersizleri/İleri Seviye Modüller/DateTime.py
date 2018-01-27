from datetime import datetime
import locale

#print(datetime.now())
locale.setlocale(locale.LC_ALL, 'tr_TR') #local bilgisini değiştirir
suan = datetime.now()
print(suan.year)
print(suan.month)
print(suan.day)

print(suan.hour)
print(suan.minute)
print(suan.second)

print(datetime.ctime(suan))
print(datetime.strftime(suan,"%Y"))
print(datetime.strftime(suan,"%B"))
print(datetime.strftime(suan,"%A"))
print(datetime.strftime(suan,"%X"))
print(datetime.strftime(suan,"%D"))
print(datetime.strftime(suan,"%B %Y"))
print(datetime.strftime(suan,"%Y %B %A"))

print(suan)
saniye = datetime.timestamp(suan)
print(saniye)
suan2 = datetime.fromtimestamp(saniye)
print(suan2)

suan = datetime.fromtimestamp(0) #baz tarih bilgisi
print(suan)

tarih = datetime(2023, 1, 2)
suan = datetime.now()
print(tarih - suan)