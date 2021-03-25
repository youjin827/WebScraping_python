import requests
url = "http://2youz.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("youz.html","w", encoding="utf8") as f:
    f.write(res.text)


# user-Agent 라는 헤더 정보를 줌으로써 크롬에서 검색했을 때와 동일한 결과를 가질 수 있다.
# 이렇게 해야 제대로 된 웹스크래핑 할 수 있다. 
