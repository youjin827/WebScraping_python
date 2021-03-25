# 웹에서 원하는 정보를 추출할 때 웹페이지의 문서정보 (웹페이지의 정보)를 가져올 수 있게 하는 라이브러리
import requests


res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")

res.raise_for_status()
print(len(res.text))

with open("mygoogle.html","w", encoding="utf8") as f:
    f.write(res.text)




    
#print("응답코드 : ", res.status_code) #200 이면 정상

#if res.status_code == requests.codes.ok:
#    print("정상입니다.")
#else:
#    print("문제가 없습니다.")

#res.raise_for_status()
#print("웹 스크래핑을 진행합니다.")
