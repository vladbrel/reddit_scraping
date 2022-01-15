import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://www.reddit.com/user/NiceCasualRedditGuy/'
# page = requests.get(url)
# with open('exp_user.html', 'w', encoding='utf-8') as file:
#     file.write(page.text)
# with open('exp_user.html', encoding='utf-8') as file:
#     src = file.read()
# soup = BeautifulSoup(src, 'lxml')
# cake_day = soup.find_all("span", class_="_1hNyZSklmcC7R_IfCUcXmZ")
# print(cake_day)


driver = webdriver.Chrome( executable_path=r'D:\Vlad\Python Projects\reddit_scraping\chrome_driver\chromedriver.exe')
driver.get(url)
time.sleep(3)
with open('exp1_user.html', 'w', encoding='utf-8') as file:
    file.write(driver.page_source)
with open('exp1_user.html', encoding='utf-8') as file:
    src = file.read()
soup = BeautifulSoup(src, 'lxml')
cake_day = soup.find("span", id="profile--id-card--highlight-tooltip--cakeday")
karma = soup.find('span', id="profile--id-card--highlight-tooltip--karma")
print(cake_day.text)
print(karma.text)

#<span id="profile--id-card--highlight-tooltip--karma" class="_1hNyZSklmcC7R_IfCUcXmZ">45,615</span>
