# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import musinsa_youngji

# 브라우저 설치

webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
# ChromeDriver 실행

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 https://www.w3schools.com/ 입력
# browser.get("https://www.musinsa.com/app/goods/2338457")                                                       #url 가장 먼저 입력          끝

# - 가능 여부에 대한 OK 받음 (ok를 주고받는 네트워크 상 번호는 200이다.)
pass
# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)                                                                       #페이지 접속 가정
#######################################################################################################

# 정보 획득

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 

# mongodb 연결
def Connectdb(collection_name):
    from pymongo import MongoClient
    mongoClient = MongoClient("mongodb://localhost:27017")
    database = mongoClient["gatheringdatas"]
    collection = database[collection_name]
    return collection

    
# for page_number in range(3,len(element_total_page)-1) :                                                      #페이지 넘버 별로 클릭하기 위해 순서
# element_total_page = browser.find_elements(by = By.CSS_SELECTOR,value = "div.pagination.textRight > div.wrapper > a.paging-btn.btn")  
def information(collection) :
    
    element_name = browser.find_elements(by = By.CSS_SELECTOR, value = "p.review-profile__name")                      # 닉네임 리스트
    element_detail = browser.find_elements(by = By.CSS_SELECTOR, value = "div.review-goods-information__item")        # 구매 정보 리스트
    try :
        element_comment = browser.find_elements(by = By.CSS_SELECTOR, value = "div.review-contents__text")                # 댓글 리스트
        pass
    except:
        element_comment = ""          
        pass
#     return element_name,element_detail,element_comment


# 
# def review(element_name,element_detail,element_comment,collection,inserted_id) :
    # inserted_id = musinsa_youngji.getElement(browser, collection)
    for index in range(len(element_name)) :                                                                 #닉네임 리스트 수에 매치하여 세부정보,댓글을 출력

        name = element_name[index].text
        detail = element_detail[index].text
        comment = element_comment[index].text
        
    
        collection.insert_one({"닉네임": name,"구매정보": detail, "댓글": comment})
    return 0

if __name__ == "__main__":
    try:
        browser.get("https://www.musinsa.com/app/goods/2338457")     
        collection = Connectdb("musinsa_review")
        information(collection)
    except:
        pass
    finally :
        pass

# element_name,element_detail,element_comment = information()
# review(element_name,element_detail,element_comment,collection)

# inserted_review = review(collection)

# information(inserted_id,inserted_review)

#         if page_number < len(total_page) :
#             time.sleep(10)
#             total_page[page_number].click()
#             time.sleep(2)
#         else :
#             break
# pass

#페이지번 호가 안돌음

# Exception has occurred: ElementClickInterceptedException
# Message: element click intercepted: Element <a href="javascript:void(0);" class="paging-btn btn" onclick="ReviewPage.goPage(...); return false;">2</a> is not clickable at point (895, 844). Other element would receive the click: <div class="sc-1n9z06l-0 gUyyNW">...</div>
#   (Session info: chrome=120.0.6099.130)




