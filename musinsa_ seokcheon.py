# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# 브라우저 설치

webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 https://www.w3schools.com/ 입력
browser.get("https://www.musinsa.com/app/goods/2338457")                                                       #url 가장 먼저 입력          끝

# - 가능 여부에 대한 OK 받음 (ok를 주고받는 네트워크 상 번호는 200이다.)
pass
# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)                                                                       #페이지 접속 가정
#######################################################################################################

# 정보 획득

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 

total_page = browser.find_elements(by = By.CSS_SELECTOR,value = "div.page2 > a > span") 

element_name = browser.find_element(by = By.CSS_SELECTOR, value = "p.review-profile__name")                      # 닉네임
element_name.text

element_detail = browser.find_element(by = By.CSS_SELECTOR, value = "div.review-goods-information__item")        # 세부 정보
element_name.text

try :
    element_comment = browser.find_element(by = By.CSS_SELECTOR, value = "div.review-contents__text")                # 댓글
    element_comment.text
    pass
except:
    comments = ""          
    pass
finally:
    pass





