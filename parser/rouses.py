import requests
import fake_useragent
from bs4 import BeautifulSoup
from time import sleep
import json

user = fake_useragent.UserAgent().random

header = {'user-agent': user}



def collect_data_rouse_1():
    '''parse about bouquets of roses from crocus24.by '''
    data = []

    for p in range(1, 6):
        print(p)
        url = f"https://crocus24.by/bukety/bukety-s-rozami/?page={p}"
        responce = requests.get(url, headers = header).text
        sleep(0.1)
        soup = BeautifulSoup(responce, 'lxml')

        flowers = soup.find_all("div", class_ = 'product-thumb')
        

        
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
            
    with open('data/rouse_buq_1.json', 'w') as file:
        json.dump(data, file, indent=3, ensure_ascii=False)
    

            
    return data


    

def collect_data_rouse_2():
    '''parse about bouquets of roses from buketti.by '''
    
    data_2 = []

    for p in range(0, 58):
        print(p)

        
        url = f"https://buketti.by/catalog/bukety-roz?page={p}"
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

    with open('data/rouse_buq_2.json', 'w') as file:
        json.dump(data_2, file, indent=3, ensure_ascii=False)
    
        
    return data_2




def collect_data_rouses_all():
    data = collect_data_rouse_1()
    datatwo = collect_data_rouse_2()
   




def main():
    collect_data_rouses_all()


if __name__ == '__main__':
    main()