import requests
from bs4 import BeautifulSoup

url = 'https://store.steampowered.com/search/?specials=1' 

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  
    soup = BeautifulSoup(response.text, 'lxml')
    page_title = soup.title.string
    print(f"Заголовок сайта: {page_title}\n")

    
    #links = soup.find_all('a', limit=5) #
    
    #print("Первые 5 ссылок на странице:")
    #for link in links:
        #href = link.get('href')
        #text = link.text.strip()
        #print(f"- {text}: {href}")

    print("-------------------------------------------------------------")
    
    sells = soup.find("span", class_="title")
    print(sells)
    

except Exception as e:
    print(f"Произошла ошибка: {e}")