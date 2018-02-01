import requests
import sys

url = "http://api.fixer.io/latest?base="

birinci_doviz = input("Birinci Dövizi Giriniz:")
ikinci_doviz = input("İkinci Dövizi Giriniz:")
miktar = float(input("Döviz Miktarı Giriniz:"))

response = requests.get(url + birinci_doviz)

#print(response)

json_verisi = response.json()

#print(json_verisi)
try:
    print("{} {} {} {}".format(miktar,birinci_doviz,json_verisi["rates"][ikinci_doviz] * miktar,ikinci_doviz))
except KeyError:
    sys.stderr.write("Lüften Para Birimini Doğru Giriniz")
    sys.stderr.flush()
