import uuid
import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup

exe_path = r'D:\Vlad\Python Projects\reddit_scraping\chrome_driver\chromedriver.exe'
def get_main_page(ep):
    driver = webdriver.Chrome( executable_path=ep)
    try:
        driver.get('https://www.reddit.com/top/?t=month')
        time.sleep(0.1)
        with open('data/top_month.html', 'w', encoding='utf-8') as file:
            file.write(driver.page_source)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
#get_main_page()

posts_urls= []
def collect_post_urls(size):
    if size == 'big':
        page = 'data/top_month_big.html'
    else:
        page = 'data/top_month.html'
    with open(page, encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    posts = soup.find_all(class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE")
    all_posts_dict = {}
    for item in posts:
        item_text = item.text
        if '*' in item_text:
            item_text = item_text.replace('*', '_')
        item_url = 'http://www.reddit.com' + item.get('href')
        all_posts_dict[item_text] = item_url
        posts_urls.append(item_url)
        print(f'{item_text}:{item_url}')
    print(posts_urls)
    return posts_urls
#collect_post_urls()

def record_post_pages():
    count = 0
    for url in posts_urls:
        req = requests.get(url)
        with open(f'data/{count}.html', 'w', encoding='utf-8') as file:
            file.write(req.text)
        count+=1
# def record_post_pages(ep):
#     driver = webdriver.Chrome( executable_path=ep)
#     count = 0
#     try:
#        for url in posts_urls:
#            try:
#                driver.get(url)
#                time.sleep(0.5)
#                with open(f'data/{count}.html', 'w',encoding='utf-8') as file:
#                    file.write(driver.page_source)
#                count=count+1
#            except:
#                continue
#     except Exception as ex:
#        print(ex)
#     finally:
#        driver.close()
#        driver.quit()
#record_post_pages()

user_list_for_comm_and_post_karma=[]
user_list_for_cake_day = []
def collect_user_urls(size):
    if size == 'big':
        page = 'data/top_month_big.html'
    else:
        page = 'data/top_month.html'
    with open(page, encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml', multi_valued_attributes=None)
    users = soup.find_all('a', class_="_2tbHP6ZydRpjI44J3syuqC  _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE")
    for item in users:
        user_url = item.get('href')
        user_list_for_comm_and_post_karma.append('https://www.reddit.com/'+user_url)
        user_list_for_cake_day.append('https://www.reddit.com'+user_url)
        print(user_url)
        username = user_url[6:-1]
        print(username)
    print(user_list_for_comm_and_post_karma)
    print(user_list_for_cake_day)
#collect_user_urls()

def record_user_pages_comm_post_karma():
    count = 0
    for user in user_list_for_comm_and_post_karma:
        req = requests.get(user)
        with open(f'data/users_post_comment_karma/{count}.html', 'w', encoding='utf-8') as file:
            file.write(req.text)
        count+=1
# def record_user_pages_comm_post_karma(ep):
#     driver = webdriver.Chrome( executable_path=ep)
#     try:
#         count = 0
#         for user in user_list_for_comm_and_post_karma:
#             try:
#                 driver.get(user)
#                 time.sleep(0.5)
#                 with open(f'data/users_post_comment_karma/{count}.html', 'w', encoding='utf-8') as file:
#                     file.write(driver.page_source)
#                 count+=1
#             except:
#                 continue
#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()
#record_user_pages_comm_post_karma()

def record_user_pages_cake_day():
    count = 0
    for user in user_list_for_cake_day:
        req = requests.get(user)
        with open(f'data/users_post_comment_karma/{count}.html', 'w', encoding='utf-8') as file:
            file.write(req.text)
        count+=1
# def record_user_pages_cake_day(ep):
#     driver = webdriver.Chrome( executable_path=ep)
#     try:
#         count = 0
#         for user in user_list_for_cake_day:
#             try:
#                 driver.get(user)
#                 time.sleep(0.5)
#                 with open(f'data/users_cake_day/{count}.html', 'w', encoding='utf-8') as file:
#                     file.write(driver.page_source)
#                 count +=1
#             except:
#                 continue
#     except Exception as ex:
#         print(ex)
#     finally:
#         driver.close()
#         driver.quit()
#record_user_pages_cake_day()

def get_user_for_cake_day(x):
    count = 0
    for user in range(x):
        with open(f'data/users_cake_day/{user}.html', encoding='utf-8') as file:
            src = file.read()
        soup = BeautifulSoup(src, 'lxml', multi_valued_attributes=None)
        try:
            cake_day = soup.find("span", id="profile--id-card--highlight-tooltip--cakeday")
            karma = soup.find('span', id="profile--id-card--highlight-tooltip--karma")
            print(cake_day.text)
            print(karma.text)
        except:
            continue
        count +=1
#get_user_for_cake_day(len(user_list_for_cake_day))

def get_user_for_comment_post_karma(x):
    count = 0
    for user in range(x):
        with open(f'data/users_post_comment_karma/{user}.html', encoding='utf-8') as file:
            src = file.read()
        soup = BeautifulSoup(src, 'lxml', multi_valued_attributes=None)
        try:
            post_karma = soup.find("span", class_='karma')
            comment_karma = soup.find('span', class_="karma comment-karma")
            print(post_karma.text)
            print(comment_karma.text)
        except:
            continue
        count +=1
#get_user_for_comment_post_karma(len(user_list_for_comm_and_post_karma))

list_num_of_votes = []
def get_num_votes(x):
    for count in range(x):
        try:
            with open(f'data/{count}.html', encoding='utf-8') as file:
                src = file.read()
            soup = BeautifulSoup(src, 'lxml')
            num_votes = soup.find('div', class_="_1E9mcoVn4MYnuBQSVDt1gC")
            print(num_votes.text)
            list_num_of_votes.append(num_votes.text)

        except:
            continue
#get_num_votes(len(posts_urls))
#print(list_num_of_comm)

list_num_of_comments = []
def get_num_comments(x):
    for count in range(x):
        try:
            with open(f'data/{count}.html', encoding='utf-8') as file:
                src = file.read()
            soup = BeautifulSoup(src, 'lxml')
            num_comments = soup.find('span', class_="FHCV02u6Cp2zYL0fhQPsO")
            print(num_comments.text)
            list_num_of_comments.append(num_comments.text)
        except:
            continue
#get_num_comments(len(posts_urls))

list_category = []
def get_category(x):
    for count in range(x):
        try:
            with open(f'data/{count}.html', encoding='utf-8') as file:
                src = file.read()
            soup = BeautifulSoup(src, 'lxml')
            category = soup.find('div', class_="_3CUdiRoAXQxoYJ-UeFCjPS _2SVIoeexI3lRGCH0NAYAMx")
            print(category.text)
            list_category.append(category.text)
        except:
            continue
#get_category(len(posts_urls))

list_post_date = []
def get_post_date(x):
    for count in range(x):
        try:
            with open(f'data/{count}.html', encoding='utf-8') as file:
                src = file.read()
            soup = BeautifulSoup(src, 'lxml')
            post_date = soup.find('a', class_='_3jOxDPIQ0KaOWpzvSQo-1s')
            print(post_date.text)
            list_post_date.append(post_date.text)
        except:
            continue
#get_post_date(len(posts_urls))

list_id = []
# def get_Unique_id(x):
#     count = 0
#     for count in range(x):
#         ui = uuid.uuid1().hex
#         print(ui)
#         list_id.append(ui)
#         count +=1
# get_Unique_id(len(posts_urls))
def add_ud(x):
    for i in range(x):
        tu = [i]
        tu.append(uuid.uuid1().hex)
        print(tu)
#add_ud(5)

def get_big_main_page(ep):
    driver = webdriver.Chrome(executable_path=ep)
    try:
        driver.get('https://www.reddit.com/top/?t=month')
        for i in range(60):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(0.1)
            i+=1
        with open('data/top_month_big.html', 'w', encoding='utf-8') as file:
            file.write(driver.page_source)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
#get_big_main_page()

