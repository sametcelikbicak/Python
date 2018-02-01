import requests
from bs4 import BeautifulSoup

url = "http://www.imdb.com/chart/top"

response = requests.get(url)
#print(response)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

basliklar = soup.find_all("td",{"class":"titleColumn"})
ratings = soup.find_all("td",{"class":"ratingColumn imdbRating"})

#print(len(basliklar),len(ratings))



for baslik,rating in zip(basliklar,ratings):
    baslik = baslik.text
    rating = rating.text
    baslik = baslik.strip()
    baslik = baslik.replace("\n","")
    rating = rating.strip()
    rating = rating.replace("\n","")

    print("Film Adı: {} Rating: {}".format(baslik,rating))
    print("*************************************")