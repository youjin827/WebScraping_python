from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe") # 실행파일 경로 다르면 () 안에 경로 넣어줘야 함.
browser.get("http://naver.com")  # 위의 브라우저에서 현 행 괄호 안의 url 로 이동.


