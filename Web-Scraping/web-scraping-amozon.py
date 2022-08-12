import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com.tr/b?ie=UTF8&node=15290783031"

html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")

list = soup.find_all("div",{"class":"a-section a-spacing-small s-padding-left-small s-padding-right-small"},limit=1)
count = 1
for div in list:
    name =div.h2.a.span.text
    fiyat = div.find("span",{"class":"a-price-whole"})
    link = div.a.get("href").strip("<>")
    print(f"Marka: {name} Fiyat: {fiyat} Urun Link:{link}")
    count += 1
# name = div.find("div",{"class":"p-card-img"}).find_all("a")[0]
    