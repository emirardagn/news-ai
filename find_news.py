import requests
from bs4 import BeautifulSoup


def find_news():
    url = "https://www.google.com/search?q=ai+news&sca_esv=87cd9f5db8b9fddc&sca_upv=1&tbm=nws&sxsrf=ADLYWIIgTdfC4G7lXkZYiFpq91G8qKxXyA:1723099882057&source=lnt&tbs=qdr:d&sa=X&ved=2ahUKEwi3sYej5-SHAxWLQvEDHdGeA-YQpwV6BAgEEA0&biw=1854&bih=961&dpr=1"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url,headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    div_content = soup.find_all('div', class_='Gx5Zad')


    with open("index.html", 'w', encoding='utf-8') as file:
        file.write(str(soup))

    news = []
    for d in div_content:
        try:
            title = d.find("h3").get_text()
            link = d.a['href']
            link = link.split("U&url=")[1]
            link = link.split("&ved=2ah")[0]
            img = d.find("img")["src"]
            news.append({
                'title': title,
                'link': link,
                'img': img
            })
            
        except:
            _=1
    print("Bulunan haber sayısı:", len(news))
    return news