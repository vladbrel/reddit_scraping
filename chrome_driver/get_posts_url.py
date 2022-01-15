import requests
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
#get_main_page()

posts_urls= []
def collect_post_urls(x):
    with open(x, encoding='utf-8') as file:
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
collect_post_urls(get_main_page())


def record_post_pages():
    driver = webdriver.Chrome( executable_path=r'D:\Vlad\Python Projects\reddit_scraping\chrome_driver\chromedriver.exe')
    count = 0
    try:
       for url in posts_urls:
           try:
               driver.get(url)
               time.sleep(2)
               with open(f'data/{count}.html', 'w',encoding='utf-8') as file:
                   file.write(driver.page_source)
               count=count+1
           except:
               continue
    except Exception as ex:
       print(ex)
    finally:
       driver.close()
       driver.quit()
#record_post_pages()

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
#collect_user_urls()

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
#record_user_pages_comm_post_karma()

def record_user_pages_cake_day():
    driver = webdriver.Chrome( executable_path=r'D:\Vlad\Python Projects\reddit_scraping\chrome_driver\chromedriver.exe')
    try:
        count = 0
        for user in user_list_for_cake_day:
            try:
                driver.get(user)
                time.sleep(1)
                with open(f'data/users_cake_day/{count}.html', 'w', encoding='utf-8') as file:
                    file.write(driver.page_source)
                count +=1
            except:
                continue
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
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
#get_user_for_comment_post_karma(len(user_list_for_comm_and_post_karma)
#<div class="_1E9mcoVn4MYnuBQSVDt1gC" id="vote-arrows-t3_r8s8py"><button aria-label="upvote" aria-pressed="false" class="voteButton " data-click-id="upvote" id="upvote-button-t3_r8s8py"><span class="_2q7IQ0BUOWeEZoeAxN555e _3SUsITjKNQ7Tp0Wi2jGxIM qW0l8Af61EP35WIG6vnGk _3edNsMs0PNfyQYofMNVhsG"><i class="icon icon-upvote _2Jxk822qXs4DaXwsN7yyHA"></i></span></button><div class="_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo " style="color:#1A1A1B">126k</div><button aria-label="downvote" aria-pressed="false" class="voteButton" data-click-id="downvote"><span class="_1iKd82bq_nqObFvSH1iC_Q Q0BxYHtCOJ_rNSPJMU2Y7 _2fe-KdD2OM0ciaiux-G1EL _3yQIOwaIuF6gn8db96Gu7y"><i class="icon icon-downvote ZyxIIl4FP5gHGrJDzNpUC"></i></span></button></div>
#<div class="_1E9mcoVn4MYnuBQSVDt1gC" id="vote-arrows-t3_rzv4hw"><button aria-label="upvote" aria-pressed="false" class="voteButton " data-click-id="upvote" id="upvote-button-t3_rzv4hw"><span class="_2q7IQ0BUOWeEZoeAxN555e _3SUsITjKNQ7Tp0Wi2jGxIM qW0l8Af61EP35WIG6vnGk _3edNsMs0PNfyQYofMNVhsG"><i class="icon icon-upvote _2Jxk822qXs4DaXwsN7yyHA"></i></span></button><div class="_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo " style="color:#1A1A1B">180k</div><button aria-label="downvote" aria-pressed="false" class="voteButton" data-click-id="downvote"><span class="_1iKd82bq_nqObFvSH1iC_Q Q0BxYHtCOJ_rNSPJMU2Y7 _2fe-KdD2OM0ciaiux-G1EL _3yQIOwaIuF6gn8db96Gu7y"><i class="icon icon-downvote ZyxIIl4FP5gHGrJDzNpUC"></i></span></button></div>
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
get_num_votes(len(posts_urls))
#print(list_num_of_comm)
#<span class="FHCV02u6Cp2zYL0fhQPsO">863 comments</span>
list_num_of_comments = []
def get_num_comments(x):
    for count in range(x):
        try:
            with open(f'data/{count}.html', encoding='utf-8') as file:
                src = file.read()
            soup = BeautifulSoup(src, 'lxml')
            num_votes = soup.find('span', class_="FHCV02u6Cp2zYL0fhQPsO")
            print(num_votes.text)
            list_num_of_votes.append(num_votes.text)

        except:
            continue
get_num_votes(len(posts_urls))



