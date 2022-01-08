from selenium import webdriver
import time
from bs4 import BeautifulSoup


# def get_main_page():
#     driver = webdriver.Chrome( executable_path=r'D:\Vlad\Python Projects\reddit_scraping\chrome_driver\chromedriver.exe')
#     try:
#         driver.get('https://www.reddit.com/top/?t=month')
#         time.sleep(2)
#         with open('top_month.html', 'w', encoding='utf-8') as file:
#             file.write(driver.page_source)
#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()
#<div class="y8HYJ-y_lTUHkQIc1mdCq _2INHSNB8V5eaWp4P0rY_mE"><a data-click-id="body" class="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE" href="/r/facepalm/comments/rwu6x4/adult_tantrum/"><div class="_2SdHzo12ISmrC8H86TgSCp _3wqmjmv3tb_k-PROt7qFZe " style="--posttitletextcolor:#222222;"><h3 class="_eYtD2XCVieq6emjKBH3m">Adult tantrum</h3></div></a></div>
#<div class="_2SdHzo12ISmrC8H86TgSCp _3wqmjmv3tb_k-PROt7qFZe " style="--posttitletextcolor:#222222;"><h3 class="_eYtD2XCVieq6emjKBH3m">Adult tantrum</h3></div>
# get_main_page()
#
#

# collect post_urls
# with open('top_month.html', encoding='utf-8') as file:
#     src = file.read()
# soup = BeautifulSoup(src, 'lxml')
# posts = soup.find_all(class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE")
# all_posts_dict = {}
# posts_urls=[]
# for item in posts:
#     item_text = item.text
#     if '*' in item_text:
#         item_text = item_text.replace('*', '_')
#     item_url = 'http://www.reddit.com' + item.get('href')
#     all_posts_dict[item_text] = item_url
#     posts_urls.append(item_url)
#     print(f'{item_text}:{item_url}')
# print(posts_urls)

# record post pages
# driver = webdriver.Chrome( executable_path=r'D:\Vlad\Python Projects\reddit_scraping\chrome_driver\chromedriver.exe')
# count = 0
# try:
#    for url in posts_urls:
#        try:
#            driver.get(url)
#            time.sleep(2)
#            with open(f'data/{count}.html', 'w',encoding='utf-8') as file:
#                file.write(driver.page_source)
#            count=count+1
#        except:
#            continue
# except Exception as ex:
#    print(ex)
# finally:
#    driver.close()
#    driver.quit()
#<div class="_2mHuuvyV9doV3zwbZPtIPG"><a class="_2tbHP6ZydRpjI44J3syuqC  _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" href="/user/thefakerealdrpepper/" style="color: rgb(120, 124, 126);">u/thefakerealdrpepper</a><div id="UserInfoTooltip--t3_rt5ra5"></div></div>


# collect user_urls
with open('top_month.html', encoding='utf-8') as file:
    src = file.read()
soup = BeautifulSoup(src, 'lxml', multi_valued_attributes=None)
users = soup.find_all('a',class_="_2tbHP6ZydRpjI44J3syuqC  _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE")
user_list=[]
for item in users:
    user_url = 'https://www.reddit.com/'+item.get('href')
    user_list.append(user_url)
    print(user_url)

#<div class="_2mHuuvyV9doV3zwbZPtIPG"><a class="_2tbHP6ZydRpjI44J3syuqC  _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" href="/user/asianj1m/" style="color: rgb(120, 124, 126);">u/asianj1m</a><div id="UserInfoTooltip--t3_rxfzz6"></div></div>
#<div class="_2mHuuvyV9doV3zwbZPtIPG"><a class="_2tbHP6ZydRpjI44J3syuqC  _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE" href="/user/asianj1m/" style="color: rgb(120, 124, 126);">u/asianj1m</a><div id="UserInfoTooltip--t3_rxfzz6"></div></div>
#
# record user pages
# print(user_list)
driver = webdriver.Chrome( executable_path=r'D:\Vlad\Python Projects\reddit_scraping\chrome_driver\chromedriver.exe')
try:
    count = 0
    for user in user_list:
        try:
            driver.get(user)
            time.sleep(5)
            with open(f'data/{count}_user.html', 'w', encoding='utf-8') as file:
                file.write(driver.page_source)
            count+=1
        except:
            continue
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
num_users = len(user_list)
#num_users = 14
#<span id="profile--id-card--highlight-tooltip--karma" class="_1hNyZSklmcC7R_IfCUcXmZ">83,810</span>
# get user karma
count = 0
for item in range(num_users):
    with open(f'data/{count}_user.html', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src,'lxml')
    user_karma = soup.find('span', class_='_1hNyZSklmcC7R_IfCUcXmZ')
    print(user_karma)
    count+=1