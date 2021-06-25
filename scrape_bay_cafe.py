import requests
from bs4 import BeautifulSoup

url = 'https://skylink-pro.com/remote-index.php?domainname=baycafe&keyword=parade'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

page_section = soup.find(id='col2')

headers = page_section.find_all('div', class_='databoxDataHeader')
data = page_section.find_all('div', class_='databoxNumber')

print(headers)
print(data)