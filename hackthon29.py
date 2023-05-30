from bs4 import BeautifulSoup
import requests
import csv


url ='https://www.mashina.kg/search/all/'
def write_csv(data):
    with open ('mashina.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['name'],data['price'],data['description'], data['image']])


def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    mashin1 = soup.find_all("div", class_ ="list-item list-label")

    for i in mashin1:
        title = i.find("h2", class_="name").text.replace(' ', '')
        price = i.find("p").text.replace(' ', '')
        description = i.find("div", class_="block info-wrapper item-info-wrapper").text.replace(' ', '')
        image = i.find('div',class_ = 'thumb-item-carousel').find('img', class_='lazy-image').get('data-src')
        dict_ = {"name":title, "price":price, "description":description, "image":image}
        
        write_csv(dict_)


print(get_data(get_html(url)))
