from get_posts_url import user_list
from selenium import webdriver
import time
from bs4 import BeautifulSoup


# print(user_list)
# driver = webdriver.Chrome( executable_path=r'D:\Vlad\Python Projects\reddit_scraping\chrome_driver\chromedriver.exe')
# try:
#     count = 0
#     for user in user_list:
#         try:
#             driver.get(user)
#             time.sleep(1)
#             with open(f'data/{count}_user.html', 'w', encoding='utf-8') as file:
#                 file.write(driver.page_source)
#             count+=1
#         except:
#             continue
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()

#<span id="profile--id-card--highlight-tooltip--karma" class="_1hNyZSklmcC7R_IfCUcXmZ">83,810</span>
with open('data/0_user.html') as file:
    src = file.read()
soup = BeautifulSoup(src,'lxml')
user_karma = soup.find('span', class_='_1hNyZSklmcC7R_IfCUcXmZ')
print(user_karma)