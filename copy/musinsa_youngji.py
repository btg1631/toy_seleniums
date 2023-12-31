# https://www.musinsa.com/app/

# * 웹 크롤링 동작
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

#  uri에 의한 Browser 가져오기
def getBrowserFromURI(uri):
    webdriver_manager_directory = ChromeDriverManager().install()
    browser = webdriver.Chrome(service=ChromeService(webdriver_manager_directory))
    browser.get(uri)    # - 주소 입력
    return browser

def clickCategory(browser):
    # 카테고리 클릭 : div:nth-child(1) > div.sc-8hpehb-7.liOFHO > ul > li:nth-child(1) > a
    category = browser.find_element(by=By.CSS_SELECTOR, value="div:nth-child(1) > div.sc-8hpehb-7.liOFHO > ul > li:nth-child(1) > a")
    category.click()

# 제품 클릭
def clickElement(browser, index):
    # # for element in element_bundle[0:5]:
    # for index in range(4):
    element_bundle = browser.find_elements(by=By.CSS_SELECTOR, value="a.img-block")
    element_bundle[index].click()
    time.sleep(1)

# 제품 정보 저장
def getElement(browser):
    # 제품 이름 : div.right_contents.section_product_summary > span > em
    element_title = browser.find_element(by=By.CSS_SELECTOR, value="div.right_contents.section_product_summary > span > em").text
    # 브랜드 strong > a
    element_brand = browser.find_element(by=By.CSS_SELECTOR, value="strong > a").text
    # 판매가 #goods_price > del
    try:
        element_price = browser.find_element(by=By.CSS_SELECTOR, value="#goods_price > del").text
    except:
        element_price = browser.find_element(by=By.CSS_SELECTOR, value="#goods_price").text
    # 회원가 a > #list_price
    element_membership_fee = browser.find_element(by=By.CSS_SELECTOR, value="a > #list_price").text

    print("title : {}, brand : {}, price : {}, membership fee : {}".format(element_title, element_brand, element_price, element_membership_fee))
    time.sleep(3)

# 뒤로가기
def backElement(browser):
    browser.back()
    time.sleep(3)

# 브라우저 종료
def quitBrowser(browser):
    browser.quit()
    

if __name__ == "__main__":
    try:
        browser = getBrowserFromURI("https://www.musinsa.com/app/")
        collection = Connectdb("musinsa_item")
        clickElement(browser, collection)
        element_id = getElement(browser, collection)
    except:
        pass
    finally :
        quitBrowser(browser)
