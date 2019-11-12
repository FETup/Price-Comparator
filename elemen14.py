from bs4 import BeautifulSoup
import requests


elemcol1 = []
elemcol2 = []

url = "https://in.element14.com/search?st=PIC12F1571"

headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

page = requests.get(url,headers=headers)

soup = BeautifulSoup(page.content,'html.parser')


for point in soup.findAll('td',attrs = {'class':'productImage mftrPart'},limit=3):
    point = point.find('input').get('value')
    point = "".join(point)
    elemcol1.append(point)

for point in soup.findAll('td', attrs = {'class':'productImage mftrPart'},limit = 3):
    elemcol2.append(point.find('a').get('href'))


print(elemcol2)