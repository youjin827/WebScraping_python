# 헤드라인 뉴스 스크래핑하기

# import weather
import requests
from bs4 import BeautifulSoup





def create_soup(url):    # url 접속하는 함수
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_headline_news() :
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/main/home.nhn"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=4)
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print("{}. {}".format(index+1, title))
        print("  (링크 : {})".format(link))
    print()




if __name__ == "__main__":
    scrape_headline_news()