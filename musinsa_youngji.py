# https://www.musinsa.com/app/

# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

webdriver_manager_directory = ChromeDriverManager().install()

# ChromeDriver 실행
browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))

# Chrome WebDriver의 capabilities 속성 사용
capabilities = browser.capabilities

# - 주소 입력
browser.get("https://www.musinsa.com/app/")


# - 정보 획득
# 카테고리 클릭 : div:nth-child(1) > div.sc-8hpehb-7.liOFHO > ul > li:nth-child(1) > a
category = browser.find_element(by=By.CSS_SELECTOR, value="div:nth-child(1) > div.sc-8hpehb-7.liOFHO > ul > li:nth-child(1) > a")
category.click()

# 제품 클릭 : a.img-block

# for element in element_bundle[0:5]:
for index in range(4):
    element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value="a.img-block")
    element_bundle[index].click()
    time.sleep(1)
    # 제품 이름 : div.right_contents.section_product_summary > span > em
    element_title = browser.find_element(by=By.CSS_SELECTOR, value="div.right_contents.section_product_summary > span > em").text
    
    # 제품 정보 저장~~
    print(element_title)


    browser.back()
    time.sleep(2)
        




# 브라우저 종료
browser.quit()


if __name__ == "__main__":
    try:
        pass    # 업무 코드
    except:
        pass    # 업무 코드 문제 발생 시 대처 코드
    finally :
        pass    # try나 except이 끝난 후 무조건 실행 코드






