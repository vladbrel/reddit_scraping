import time
import uuid
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver

ex_p = r'D:\Vlad\Python Projects\reddit_scraping\chromedriver.exe'
amount = 30

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
    p_url= []
    for item in posts:
        item_text = item.text
        if '*' in item_text:
            item_text = item_text.replace('*', '_')
        item_url = 'http://www.reddit.com' + item.get('href')
        all_posts_dict[item_text] = item_url
        p_url.append(item_url)
    return p_url

def record_post_pages(posts_urls):
    count = 0
    for url in posts_urls:
        req = requests.get(url)
        with open(f'data/{count}.html', 'w', encoding='utf-8') as file:
            file.write(req.text)
        count+=1

def collect_post(size):
    if size == 'big':
        page = 'data/top_month_big.html'
    else:
        page = 'data/top_month.html'
    with open(page, encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    posts = soup.find_all(class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE")
    posts_urls = []
    for item in posts:
        item_url = 'http://www.reddit.com' + item.get('href')
        posts_urls.append(item_url)
    return posts_urls

def collect_user_urls(size):
    user_list_for_comm_and_post_karma = []
    user_list_for_cake_day = []
    usernames = []
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
        username = user_url[6:-1]
        usernames.append(username)
    return user_list_for_comm_and_post_karma, user_list_for_cake_day, usernames
def record_user_pages_comm_post_karma():
    count = 0
    for user in user_list_for_comm_and_post_karma:
        req = requests.get(user)
        with open(f'data/users_post_comment_karma/{count}.html', 'w', encoding='utf-8') as file:
            file.write(req.text)
        count+=1

def record_user_pages_cake_day():
    count = 0
    for user in user_list_for_cake_day:
        req = requests.get(user)
        with open(f'data/users_post_comment_karma/{count}.html', 'w', encoding='utf-8') as file:
            file.write(req.text)
        count+=1

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

def get_user_for_cake_day(x):
    try:
        with open(f'data/users_cake_day/{x}.html', encoding='utf-8') as file:
            src = file.read()
        soup = BeautifulSoup(src, 'lxml', multi_valued_attributes=None)
        cake_day = soup.find("span", id="profile--id-card--highlight-tooltip--cakeday")
        karma = soup.find('span', id="profile--id-card--highlight-tooltip--karma")
        return (karma.text, cake_day.text)
    except:
        return None, None

def get_user_for_comment_post_karma(x):
    try:
        with open(f'data/users_post_comment_karma/{x}.html', encoding='utf-8') as file:
            src = file.read()
        soup = BeautifulSoup(src, 'lxml', multi_valued_attributes=None)
        post_karma = soup.find("span", class_='karma')
        comment_karma = soup.find('span', class_="karma comment-karma")
        return (post_karma.text, comment_karma.text)
    except:
        return None, None

def get_username(x):
    try:
        with open(f'data/{x}.html', encoding='utf-8') as file:
            src = file.read()
        soup = BeautifulSoup(src, 'lxml', multi_valued_attributes=None)
        user = soup.find('a',class_="_2tbHP6ZydRpjI44J3syuqC  _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE")
        user_url =user.get('href')
        username = user_url[6:-1]
        return username
    except:
        return None

def get_post_date(x):
    try:
        with open(f'data/{x}.html', encoding='utf-8') as file:
            src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        post_date = soup.find('a', class_='_3jOxDPIQ0KaOWpzvSQo-1s')
        return post_date.text
    except:
        return None

def get_num_comments(x):
    try:
        with open(f'data/{x}.html', encoding='utf-8') as file:
            src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        num_comments = soup.find('span', class_="FHCV02u6Cp2zYL0fhQPsO")
        return num_comments.text
    except:
        return None

def get_num_votes(x):
    try:
        with open(f'data/{x}.html', encoding='utf-8') as file:
            src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        num_votes = soup.find('div', class_="_1E9mcoVn4MYnuBQSVDt1gC")
        return num_votes.text
    except:
        return None

def get_category(x):
    try:
        with open(f'data/{x}.html', encoding='utf-8') as file:
            src = file.read()
        soup = BeautifulSoup(src, 'lxml')
        category = soup.find('div', class_="_3CUdiRoAXQxoYJ-UeFCjPS _2SVIoeexI3lRGCH0NAYAMx")
        return category.text
    except:
        return None

def main(ep, am):
    if am > 25:
        get_big_main_page(ep)
        s = 'big'
    else:
        get_main_page(ep)
        s = 'small'
    print('main page was got')
    post_url = collect_post_urls(s)
    record_post_pages(post_url)
    users = collect_user_urls(s)
    record_user_pages_comm_post_karma(users[1])
    record_user_pages_cake_day(users[2])
    strings = []
    count = 0
    post_url = collect_post(s)
    while len(strings) < am:
        post = []
        p_url = str(post_url[count:count+1])
        post.append(p_url[2:-2])
        username = users[2][count]
        #username = get_username(count)
        post.append(username)
        user_karma, cake_day = get_user_for_cake_day(count)
        post.append(user_karma)
        post.append(cake_day)
        post_karma, comment_karma = get_user_for_comment_post_karma(count)
        post.append(post_karma)
        post.append(comment_karma)
        post_date = get_post_date(count)
        post.append(post_date)
        num_of_comments = get_num_comments(count)
        post.append(num_of_comments)
        num_of_votes = get_num_votes(count)
        post.append(num_of_votes)
        post_category = get_category(count)
        post.append(post_category)
        if None in post:
            post.clear()
            count += 1
            continue
        post_string = uuid.uuid1().hex+';'
        for item in post:
            post_string +=item+';'
        strings.append(post_string)
        count += 1
        post.clear()
        print(f'iterationn{count}')
    date = datetime.now()
    with open(f'reddit-{date.year}{date.month}{date.day}{date.hour}{date.minute}.txt', 'w') as file:
        for post in strings:
            file.write(post+'\n')
main(ex_p, amount)