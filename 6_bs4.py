# lxml : 구문 분석하는 파서.
import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status() # 혹시 문제있으면 바로 종료할 수 있게

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title) # soup객체를 통해 옆에있는 정보에 접근 가능
# print(soup.title.get_text())

print(soup.a) # soup 가 모두 가져오면 그 중에 a 태그를 뿌려줘
              # soup 객체에서 처음 발견되는 a element 출력
print(soup.a.attrs)  # a element 의 속성 정보를 출력
'''
 attes: 딕셔너리 형태로 a 안에서
        href 는 뭐고 온클릭을 누르면 이런 동작을 한다.. 알려줌 '''

print(soup.a["href"])   # a element 의 href 속성값 정보를 출력

soup.find("a", attrs={"class":"Nbtn_upload"})
# find 함수 : 뒤의 정보에 해당하는 값중에 처음으로 발견되는 element 가져올 수 있다. 

print(soup.find(attrs={"class":"Nbtn_upload"})) # class = "Nb~ " 인 어떤 element 를 찾아줘

print(soup.find("li", attrs={"class":"rank01"}))



