import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=724815&weekday=sat" #아홉수의 우리들
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# cartoons = soup.find_all("td", attrs={"class":"title"})


'''   한 줄씩 출력해보기

title = cartoons[0].a.get_text() # 가장 최근 화의 제목
link = cartoons[0].a["href"] #속성은 대괄호!

print(title) 
print("http://comic.naver.com" + link)
'''


# 평점 구하기 
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})


 
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)

print("전체 점수 : ", total_rates)
print("평균 점수 : ", total_rates / len(cartoons))