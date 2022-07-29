### selenium 패키지 모듈 이용한 자동 크롤링
- webdriver라는 API를 통해 운영체제에 설치된 웹 브라우저를 제어하는 함수를 포함한 패키지
- selenium은 브라우저를 컨트롤하는 기능이기 때문에 webdriver 프로그램을 사용
    - webdriver는 브라우저 종류에 따라 브라우저 제작 업체에서 제공

### 관련 메서드
- get(url) : url에 접근하는 메서드<br>

- from selenium.webdriver.common.by import By
- findElement() : 코드에서 조건에 맞는 태그 중 처음 나오는 태그(find)
- findElements() : 코드에서 조건에 맞는 모든 태그(findAll)

### 단,  By를 제외한 나머지 속성명은 모두 대문자로 사용<br>
- ex)By.TAGNAME <br>

- Webdriver 객체 생성
    * driver = webdriver.Chrome(드라이버경로)
- 접근한 페이지 source 추출
    * html=diver.page_source

### webdriver 통해 script 코드 직접 실행
- driver.execute_script() 함수 - driver로 script 코드를 직접 실행

### 웹에서 업무 자동화 시켰을 경우
- 반복 중 이전 단계 완료되지 않았을 경우 에러 발생 가능 - time.sleep()으로 텀을 충분히 주어야 한다.

### 외부 파일 읽어오기
- 이름이 비슷한 같은 형식의 파일 여러 개 있을 때 한 번에 읽어오는 방법
- 관련 패키지 : glob
    - 파일 경로 및 이름을 모아서 리스트에 저장
    - * 문자 사용 가능
    - ex. 주유소*.xlsx (주유소로 시작하는 모든 xlsx 파일)