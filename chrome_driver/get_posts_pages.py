from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome import options




driver = webdriver.Chrome(executable_path=r'D:\Vlad\Python Projects\reddit_scraping\chrome_driver\chromedriver.exe')
driver.get('https://www.reddit.com/top/?t=month')







