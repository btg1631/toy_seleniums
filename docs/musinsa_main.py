import musinsa_youngji
import musinsa_seokcheon

def main() :
    try:
        uri="https://www.musinsa.com/app/"
        browser = musinsa_youngji.getBrowserFromURI(uri)
        collection = musinsa_youngji.Connectdb("musinsa_items")
        collection2 = musinsa_youngji.Connectdb("musinsa_reviews")

        musinsa_youngji.clickCategory(browser)
        for index in range(4):
            musinsa_youngji.clickElement(browser, index)
            element_id = musinsa_youngji.getElement(browser, collection)
            musinsa_seokcheon.information(browser, collection2, element_id)
            musinsa_youngji.backElement(browser)
    except:
        pass    # 업무 코드 문제 발생 시 대처 코드
    finally :
        musinsa_youngji.quitBrowser(browser)    # try나 except이 끝난 후 무조건 실행 코드

if __name__ == "__main__":
    try:
        main()
    except:
        pass
    finally :
        pass

