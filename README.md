# toy_seleniums

- 사이트 - [무신사](https://www.musinsa.com/app/)

### 구성원별 역할 기록
|이름|역할|
|--|--|
|장영지|페이지 click&back, 상품 정보 수집|
|문석천|댓글 정보 수집|

### collection
|컬렉션|설명|
|--|--|
|musinsa_items|title, brand, price, membership fee|
|musinsa_reviews|상품 id, 닉네임, 구매정보, 댓글|

### function
|이름|설명|
|--|--|
|Connectdb|mongodb 연결|
|getBrowserFromURI|uri에 의한 Browser 가져오기|
|clickCategory|카테고리 클릭|
|clickElement|상품 클릭|
|getElement|상품 정보 수집|
|information|댓글 정보 수집|
|backElement|페이지 뒤로가기|
|quitBrowser|브라우저 종료|
