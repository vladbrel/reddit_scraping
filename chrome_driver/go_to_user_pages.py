#from get_posts_url import user_list
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


# with open('data/0_user.html', encoding='utf-8) as file:
#     src = file.read()
# soup = BeautifulSoup(src,'lxml')
# user_karma = soup.find('span', class_='_1hNyZSklmcC7R_IfCUcXmZ')
# print(user_karma)
driver = webdriver.Chrome( executable_path=r'D:\Vlad\Python Projects\reddit_scraping\chrome_driver\chromedriver.exe')
try:
    if True:
        try:
            driver.get('https://www.reddit.com//user/Pazluz/')
            time.sleep(2)
            with open('data/1_user.html', 'w', encoding='utf-8') as file:
                file.write(driver.page_source)

        except:
            print(1)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


with open('data/1_user.html', encoding='utf-8') as file:
    src = file.read()
soup = BeautifulSoup(src,'lxml', multi_valued_attributes=None)
#user_karma = soup.find('span', id_="profile--id-card--highlight-tooltip--karma")
user_comment_karma = soup.find('span', class_="karma comment-karma")
user_post_karma = soup.find('span', class_="karma")
#user_cake_day = soup.find("span", class_="_1hNyZSklmcC7R_IfCUcXmZ")
print(user_karma)
print(user_comment_karma.text)
print(user_post_karma.text)
print(user_cake_day)
# cake_day = soup_3.find_all("span", class_="_1hNyZSklmcC7R_IfCUcXmZ")