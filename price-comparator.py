from bs4 import BeautifulSoup
import re
import requests


url = "https://www.digikey.in/products/en?keywords=PIC10F200T&cur=INR&lang=en"

headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0b11pre) Gecko/20110126 Firefox/4.0b11pre'}

page = requests.get(url,headers=headers)
soup = BeautifulSoup(page.content,'html.parser')

digicol4 = []
digicol6 = []

digicol1 = soup.findAll('td',attrs={'class':'tr-mfgPartNumber'},limit=3)

digicol1 = [i.text.strip() for i in digicol1]


digicol2 = soup.findAll('span',attrs={'itemprop':'name'},limit=3)
digicol2 = [point.text.strip() for point in digicol2 ]


digicol3 = soup.findAll('td',attrs={'class':'tr-description'},limit=3)
digicol3 = [point.text.strip() for point in digicol3]


for hit in soup.findAll('td',attrs={'class':'tr-minQty ptable-param'},limit=3):
    digicol4.append(hit.find('span',attrs={'class','phone'}).text.strip())


digicol5= soup.findAll('td',attrs={'class':'tr-unitPrice ptable-param'},limit=3)
digicol5 = [point.text.strip() for point in digicol5]

#digicol6 = soup.findAll('td',attrs={'class','tr-mfgPartNumber'},limit=3)
for point in soup.findAll('td',attrs={'class','tr-mfgPartNumber'},limit=3):
    digicol6.append(point.find('a').get('href'))
    

print(digicol6)   