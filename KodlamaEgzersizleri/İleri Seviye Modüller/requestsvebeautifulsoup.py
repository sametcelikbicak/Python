import requests
from bs4 import BeautifulSoup

url = "https://yellowpages.com.tr/ara?q=İzmir"
response = requests.get(url)
print(response)