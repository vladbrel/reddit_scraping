from selenium import webdriver
import time
from bs4 import BeautifulSoup

def get_main_page():
    driver = webdriver.Chrome( executable_path=r'D:\Vlad\Python Projects\reddit_scraping\chrome_driver\chromedriver.exe')
    try:
        driver.get('https://www.reddit.com/top/?t=month')
        time.sleep(2)
        with open('top_month.html', 'w', encoding='utf-8') as file:
            file.write(driver.page_source)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
    return 'top_month.html'
get_main_page()

user_list_for_comm_and_post_karma=[]
user_list_for_cake_day = []
def collect_user_urls():
    with open('top_month.html', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml', multi_valued_attributes=None)
    users = soup.find_all('a',class_="_2tbHP6ZydRpjI44J3syuqC  _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE")
    for item in users:
        user_url = item.get('href')
        user_list_for_comm_and_post_karma.append('https://www.reddit.com/'+user_url)
        user_list_for_cake_day.append('https://www.reddit.com'+user_url)
        print(user_url)
    print(user_list_for_comm_and_post_karma)
    print(user_list_for_cake_day)
collect_user_urls()

def record_user_pages_comm_post_karma():
    driver = webdriver.Chrome( executable_path=r'D:\Vlad\Python Projects\reddit_scraping\chrome_driver\chromedriver.exe')
    try:
        count = 0
        for user in user_list_for_comm_and_post_karma:
            try:
                driver.get(user)
                time.sleep(1)
                with open(f'data/users_post_comment_karma/{count}.html', 'w', encoding='utf-8') as file:
                    file.write(driver.page_source)
                count+=1
            except:
                continue
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
record_user_pages_comm_post_karma()
l_p_k =[]
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
            l_p_k.append(post_karma.text)
            #print(comment_karma.text)
        except:
            continue
        count +=1
    print(l_p_k)
get_user_for_comment_post_karma(len(user_list_for_comm_and_post_karma))





