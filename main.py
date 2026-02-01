import requests
import json #Для красивого вывода (встроенная библиотека если че).
from bs4 import BeautifulSoup

#Ссылка.
url = 'https://store.steampowered.com/search/?specials=1' 
#Агент, чтобы признали человеком.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}


try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  
    soup = BeautifulSoup(response.text, 'lxml')
    #Создание списков.
    list = []
    listprices = []
    listlinks = []
        
    #Заполнение списков с названиями игр и их цены(Со скидками).
    for sells in soup.find_all("span", class_="title"):
        list.append(sells.get_text())

    for sells in soup.find_all("div",class_="discount_final_price"):
        listprices.append(sells.get_text())
    
    #Собрал ссылки, пока без вывода
    for sells in soup.find_all("a", class_="search_result_row ds_collapse_flag"):
        listlinks.append(sells.get("href"))

    
    #Заполнение словаря.
    ddict = dict(zip(list, listprices))

    

    #Вот такой вывод получился, надо будет импортировать переменную в файл с ботом (from main import result вроде).
    result = json.dumps(ddict, indent=4, ensure_ascii=False).replace('"', '').replace(',', '')
    
        
        

except Exception as e:
    print(f"Произошла ошибка: {e}")
    
