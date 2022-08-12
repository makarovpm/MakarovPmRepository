html_doc = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk Sayfam DGL</title>
</head>
<body>
    <div class="grup1">
    <h1>Python Nedir?</h1>
    <h3>Zorluk Derecesi Nedir?</h3>
    <ul>
        <li>Python Nedir?</li>
        <li>Neden Python?</li>
        <li>Kullanım Alanları</li>
    </ul>
    </div>

    <div class="grup2">
        <h2>Programlama İçin Uygun Bir Dil Mi ?</h2>
        <ul>
            <li>Python Nedir?</li>
            <li>Neden Python?</li>
            <li>Kullanım Alanları</li>
        </ul>
    </div>
</body>
</html>
'''

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc,'html.parser')
result = soup.prettify()
# result = soup.title --> SAYFANIN BAŞLIK KISMINI ALIR
# result = soup.title.name --> title içerigini alır
# result = soup.title.string --> title içerisinde ki yazıyı gösterir
# result = soup.body --> SAYFANIN BODY KISMINI ALIR
# result = soup.find_all('h2') --> SAYFA İÇİNDE Kİ TÜM H2 ETKİKETLERİNİ GÖSTERİR
result = soup.find_all('ul')[0]
print(result)