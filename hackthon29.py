# from bs4 import BeautifulSoup
# import requests
# import csv

# URL = 'https://www.link.kg/catalog/1/'

# def write_csv(data):
#     with open('link.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow([data['data'],data['pric'],data['tuple']])

# def get_html(url):
#     response = requests.get(url)
#     return response.text

# def get_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     list_1 = soup.find_all("tr", class_ = "r1")
#     list_1 = soup.find_all("tr", class_ = "r2")

#     for i in list_1:
#         title = i.find_all("td")
#         price = i.find("td", class_ = "tp").text
#         dict_ = {"data":title[1].text, "pric":price, "tuple":title[3].text}

#         write_csv(dict_)


# print(get_data(get_html(URL)))

