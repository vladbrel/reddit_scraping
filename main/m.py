import requests
from bs4 import BeautifulSoup


url='https://www.reddit.com/top/?t=month'
#headers для того, чтоб сайт "меньше возмущался"
headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}
req = requests.get(url, headers=headers)
src =req.text
print(src)

with open('index_2.html', 'w', encoding='utf-8') as file:
    file.write(src)