import requests
from bs4 import BeautifulSoup
from time import sleep
import random
import csv

def csv_file():
  f = open('flowers.csv', 'w', newline='\n', encoding='UTF-8_sig')
  csv_object = csv.writer(f)
  csv_object.writerow([' id ', ' price ', ' status '])

def connection(url):
    resp_main = requests.get(url)
    content_main = resp_main.text
    soup = BeautifulSoup(content_main, 'html.parser')
    section = soup.find('section', {'class':"section wrapper"})
    flower_info = section.find_all('div', {'class':"catalog-box"})
    f = open('flowers.csv', 'a', newline='\n', encoding='UTF-8_sig')
    csv_object = csv.writer(f)
    for flower in flower_info:
        id = flower.p.text
        price = flower.find_all('p')[1].text 
        status = flower.find_all('p')[2].text
        csv_object.writerow([id, price, status])
    
    

def main():
 csv_file()
 for i in range(0,6):
   connection('https://flowers.ge/ka/catalogue/pg/{}/'.format(i))
   sleep(random.randint(5,15))


if __name__ == '__main__':
 main()






