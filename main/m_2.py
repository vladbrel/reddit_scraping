from bs4 import BeautifulSoup


with open('index.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

all_posts_hrefs = soup.find_all(class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE")
for item in all_posts_hrefs:
    print(item)
    item_text = item.text
    item_href = 'www.reddit.com' + item.get('href')
    print(f'{item_text}:{item_href}')
