from selenium import webdriver
import time
from bs4 import BeautifulSoup
from chrome_driver.get_posts_url import posts_urls


driver = webdriver.Chrome( executable_path=r'D:\Vlad\Python Projects\reddit_scraping\chrome_driver\chromedriver.exe')
try:

    for post_url in posts_urls:
        try:
            driver.get(post_url)
            time.sleep(2)

        except:
            continue
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
with open('data/0.html', encoding='utf-8') as file:
    src = file.read()
soup = BeautifulSoup(src, 'lxml')
post_data = soup.find('a', class_="_3jOxDPIQ0KaOWpzvSQo-1s")
print(post_data)

#<a class="_3jOxDPIQ0KaOWpzvSQo-1s" data-click-id="timestamp" href="https://www.reddit.com/r/MadeMeSmile/comments/rt5ra5/after_16_years_of_homelessness_i_finally_have_my/" style="color:#787C7E" target="_blank" rel="nofollow noopener noreferrer">10 days ago</a>