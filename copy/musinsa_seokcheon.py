# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# 브라우저 설치
webdriver_manager_directory = ChromeDriverManager().install()
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# for page_number in range(3,len(element_total_page)-1) :                       #페이지 넘버 별로 클릭하기 위해 순서
# element_total_page = browser.find_elements(by = By.CSS_SELECTOR,value = "div.pagination.textRight > div.wrapper > a.paging-btn.btn")  
def information(browser) :
    
    element_name = browser.find_elements(by = By.CSS_SELECTOR, value = "p.review-profile__name")                      # 닉네임 리스트
    element_detail = browser.find_elements(by = By.CSS_SELECTOR, value = "div.review-goods-information__item")        # 구매 정보 리스트
    try :
        element_comment = browser.find_elements(by = By.CSS_SELECTOR, value = "div.review-contents__text")                # 댓글 리스트
        pass
    except:
        element_comment = ""          
        pass

    for index in range(len(element_name)) :                       #닉네임 리스트 수에 매치하여 세부정보,댓글을 출력

        name = element_name[index].text
        detail = element_detail[index].text
        comment = element_comment[index].text
        
        print({"닉네임": name,"구매정보": detail, "댓글": comment})

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




