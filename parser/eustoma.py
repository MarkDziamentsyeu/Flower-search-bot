import requests
import fake_useragent
from bs4 import BeautifulSoup
from time import sleep
import json

user = fake_useragent.UserAgent().random

header = {'user-agent': user}


def collect_data_eustoma_1():
    '''parse about bouquets of eustoma from crocus24.by '''

    url = "https://crocus24.by/bukety/bukety-iz-eustomy/"
    responce = requests.get(url, headers = header).text
    soup = BeautifulSoup(responce, 'lxml')

    flowers = soup.find_all("div", class_ = 'product-layout')

    data = []

    for flower in flowers:
        link = flower.find('div', class_ = 'image').find('a').get('href')
        name = flower.find('div', class_ = 'caption').find('span').text
        price = flower.find('div', class_ = 'price').find('span').text
        image = flower.find('a').find('img', class_ = 'img-responsive').get('src')

        data.append(
            {
                'link': link,
                'name' : name,
                'price': price,
                'image': image
            }
        )
        
    
    with open('data/eustoma_buq_1.json', 'w') as file:
        json.dump(data, file, indent=3, ensure_ascii=False)
    

            
    return data


    

def collect_data_eustoma_2():
    '''parse about bouquets of eustoma from buketti.by '''
    
    data_2 = []

    for p in range(0, 43):
        print(p)

        
        url = f"https://buketti.by/catalog/bukety-sbornye?page={p}"
        responce = requests.get(url, headers = header).text
        sleep(0.1)
        soup = BeautifulSoup(responce, 'lxml')
        site = "https://buketti.by"



        flowers = soup.find_all('div', class_ = 'prod-teaser')

        for flower in flowers:
            link = site + flower.find('a', class_ = 'hvr-sweep-to-right').get('href')
            name = flower.find('div', class_ = 'link').find('a').text
            price = flower.find('div', class_ = 'price').find('span', class_ = 'price-tag').text.strip() + " " + flower.find('div', class_ = 'price').find('span', class_ = 'exch').text
            image = flower.find('div', class_ = 'teaser-help').find('img').get('src')

            data_2.append(
            {
                'link': link,
                'name' : name,
                'price': price,
                'image': image
            }
        )  

    with open('data/eustoma_buq_2.json', 'w') as file:
        json.dump(data_2, file, indent=3, ensure_ascii=False)
    
        
    return data_2




def collect_data_eustoma_all():
    data = collect_data_eustoma_1()
    datatwo = collect_data_eustoma_2()



def main():
    collect_data_eustoma_all()

if __name__ == '__main__':
    main()