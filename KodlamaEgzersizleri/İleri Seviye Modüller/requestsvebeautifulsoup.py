import requests
from bs4 import BeautifulSoup

url = "https://sametcelikbicak.wordpress.com"
response = requests.get(url)
#print(response.content)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

#print(soup.prettify())

#print(soup.find_all("a"))

for i in soup.find_all("a"):
    #print(i)
    #print(i.get("href"))
    print(i.text)
    print("************************************")