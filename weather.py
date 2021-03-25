# 오늘의 날씨
import requests
from bs4 import BeautifulSoup

def create_soup(url):    # url 접속하는 함수
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup
'''
def scrape_weather():
    print("[오늘의 날씨]")
    url = ("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%88%98%EC%9B%90+%EB%82%A0%EC%94%A8")
    soup = create_soup(url)

    #맑음, 어제보다 0º 더 높/작아요.
    cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()  #get_text : 소스 제외하고 문자만 가져와주는 함수

    #현재 몇도
    curr_temp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨","")
    min_temp = soup.find("span", attrs={"class":"min"}).get_text()
    max_temp =soup.find("span", attrs={"class":"max"}).get_text()


    print(cast)
    print("현재 {} (최고 {}, 최저{}).".format(curr_temp,max_temp,min_temp))

    

if __name__ == "__main__":
    scrape_weather()  # 오늘의 날씨정보 가져오기 
    '''

def scrape_headline_news() :
    print("[헤드라인 뉴스]")
    url = ("https://news.naver.com/main/home.nhn")
    soup = create_soup(url)


    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li")
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print("{}. {}".format(index+1, title))
        print("  (링크 : {})".format(link))
    print()




if __name__ == "__main__":
    scrape_headline_news