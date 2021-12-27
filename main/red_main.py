import requests
from bs4 import BeautifulSoup


# url='https://www.reddit.com/top/?t=month'
# #headers для того, чтоб сайт "меньше возмущался"
# headers = {
#     'accept': '*/*',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
# }
# req = requests.get(url, headers=headers)
# src =req.text
# print(src)

# with open('index.html', 'w', encoding='utf-8') as file:
#     file.write(src)
#/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div[5]
with open('index.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

# <a data-click-id="body" class="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE" href="/r/nextfuckinglevel/comments/rkzlrz/ups_delivery_man_goes_the_extra_level_to_hide_the/"><div class="_2SdHzo12ISmrC8H86TgSCp _3wqmjmv3tb_k-PROt7qFZe " style="--posttitletextcolor:#222222"><h3 class="_eYtD2XCVieq6emjKBH3m">UPS delivery man goes the extra level to hide the package.</h3></div></a>
# < a
# data - click - id = "body"
# class ="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE" href="/r/oddlysatisfying/comments/rfz0ir/reloading_random_objects_by_kommanderkarl/" > < div class ="_2SdHzo12ISmrC8H86TgSCp _3wqmjmv3tb_k-PROt7qFZe " style="--posttitletextcolor:#222222" > < h3 class ="_eYtD2XCVieq6emjKBH3m" > Reloading random objects by @ kommanderkarl < / h3 > < / div > < / a >

#<a data-click-id="body" class="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE" href="/r/backpacking/comments/r9elco/welcome_to_sardinia/"><div class="_2SdHzo12ISmrC8H86TgSCp _3wqmjmv3tb_k-PROt7qFZe " style="--posttitletextcolor:#222222;"><h3 class="_eYtD2XCVieq6emjKBH3m">Welcome to Sardinia</h3></div></a>

all_posts_hrefs = soup.find_all(class_="SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE")
for item in all_posts_hrefs:
    print(item)

