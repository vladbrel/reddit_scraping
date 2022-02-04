import uuid
from bs4 import BeautifulSoup
from chrome_driver.get_posts_url import get_main_page, collect_post_urls, record_post_pages, collect_user_urls, \
    record_user_pages_comm_post_karma, record_user_pages_cake_day, get_big_main_page
from datetime import datetime




def collect_post():
    with open('top_month_big.html', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    posts = soup.find_all(class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE")
    posts_urls = []
    for item in posts:
        item_url = 'http://www.reddit.com' + item.get('href')
        posts_urls.append(item_url)
    return posts_urls

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
    with open(f'data/{x}.html', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml', multi_valued_attributes=None)
    user = soup.find('a',class_="_2tbHP6ZydRpjI44J3syuqC  _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE")
    user_url =user.get('href')
    username = user_url[6:-1]
    return username

def get_post_date(x):
    with open(f'data/{x}.html', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    post_date = soup.find('a', class_='_3jOxDPIQ0KaOWpzvSQo-1s')
    return post_date.text

def get_num_comments(x):
    with open(f'data/{x}.html', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    num_comments = soup.find('span', class_="FHCV02u6Cp2zYL0fhQPsO")
    return num_comments.text

def get_num_votes(x):
    with open(f'data/{x}.html', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    num_votes = soup.find('div', class_="_1E9mcoVn4MYnuBQSVDt1gC")
    return num_votes.text

def get_category(x):
    with open(f'data/{x}.html', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    category = soup.find('div', class_="_3CUdiRoAXQxoYJ-UeFCjPS _2SVIoeexI3lRGCH0NAYAMx")
    return category.text

def main():
    #get_main_page()
    get_big_main_page()
    collect_post_urls()
    record_post_pages()
    collect_user_urls()
    record_user_pages_comm_post_karma()
    record_user_pages_cake_day()
    strings = []
    count = 0
    while len(strings) < 35:
        post = []
        post_url = collect_post()
        p_url = str(post_url[count:count+1])
        post.append(p_url[2:-2])
        username = get_username(count)
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
    date = datetime.now()
    with open(f'reddit-{date.year}{date.month}{date.day}{date.hour}{date.minute}.txt', 'w') as file:
        for post in strings:
            file.write(post+'\n')
main()