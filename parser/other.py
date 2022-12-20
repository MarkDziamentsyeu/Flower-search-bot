import requests
import fake_useragent
from bs4 import BeautifulSoup
from time import sleep
import json

user = fake_useragent.UserAgent().random

header = {'user-agent': user}




    

def collect_data_other_1():
    '''parse about other bouquets from buketti.by '''
    
    
    data = []

    for p in range(0, 43):
        print(p)

        
        url = f"https://buketti.by/catalog/bukety-sbornye?page={p}"
        responce= requests.get(url, headers = header).text
        sleep(0.1)
        soup= BeautifulSoup(responce, 'lxml')
        site = "https://buketti.by"



        flowers = soup.find_all('div', class_ = 'prod-teaser')


        for flower in flowers:
            link = site + flower.find('a', class_ = 'hvr-sweep-to-right').get('href')
            name = flower.find('div', class_ = 'link').find('a').text
            price = flower.find('div', class_ = 'price').find('span', class_ = 'price-tag').text.strip() + " " + flower.find('div', class_ = 'price').find('span', class_ = 'exch').text
            image = flower.find('div', class_ = 'teaser-help').find('img').get('src')

            data.append(
            {
                'link': link,
                'name' : name,
                'price': price,
                'image': image
            }
        )  

    with open('data/other_buq_1.json', 'w') as file:
        json.dump(data, file, indent=3, ensure_ascii=False)
    
        
    return data







def main():
    collect_data_other_1()
    

if __name__ == '__main__':
    main()