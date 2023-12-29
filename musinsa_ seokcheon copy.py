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



def pageclick():
    total_page = browser.find_elements(by = By.CSS_SELECTOR,value = "div.pagination.textRight > div.wrapper > a.paging-btn.btn") 

    for page_number in range(3,len(total_page)-2) :                                                      #페이지 넘버 별로 클릭하기 위해 순서
        total_page = browser.find_elements(by = By.CSS_SELECTOR,value = "div.pagination.textRight > div.wrapper > a.paging-btn.btn")  
        
        element_name = browser.find_elements(by = By.CSS_SELECTOR, value = "p.review-profile__name")                      # 닉네임 리스트
        element_detail = browser.find_elements(by = By.CSS_SELECTOR, value = "div.review-goods-information__item")        # 세부 정보 리스트
        try :
            element_comment = browser.find_elements(by = By.CSS_SELECTOR, value = "div.review-contents__text")                # 댓글 리스트
            pass
        except:
            comments = ""          
            pass
        finally:
            pass

        for index in range(len(element_name)) :                                                                 #닉네임 리스트 수에 매치하여 세부정보,댓글을 출력

            name = element_name[index].text
            detail = element_detail[index].text
            comment = element_comment[index].text
            
            print("{}".format(name))
            print("{}".format(detail))
            print("{}".format(comment))

        # 다음 페이지
        total_page[page_number].click()
        time.sleep(2)

while True:
    pageclick()
    total_page = browser.find_elements(by = By.CSS_SELECTOR,value = "div.pagination.textRight > div.wrapper > a.paging-btn.btn") 
    total_page[7].click()



pass





