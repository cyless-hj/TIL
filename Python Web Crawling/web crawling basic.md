### 파이썬을 이용한  웹 데이터 수집(크롤링)

1. 문서 내용 요청 후 읽어오기 urllib 패키지 
    - urlopen() 접속 
    - read() 데이터 읽어오기
    - text 속성을 사용해서 데이터 읽어올 수도 있음    
      
    

2. 문서에서 원하는 내용 추출하기(파싱)  
 
 
#### BeautifulSoup 패키지 사용 - find()/findAll()

#### urllib 패키지 - url을 넘겨주면 데이터를 텍스트 형태로 반환(기본 내장 패키지)  


- urllib2, urllib3 다른 버전 사용
- requests 패키지를 사용할 수도 있음

#### 파라미터 전달 방법
- 파라미터란? : 사이트의 문서를 요청할 때 서버로 전달되는 정보
- 함수의 파라미터 처럼 문서를 찾기위한 정보나 명령을 수행하기 위한 정보를 같이 전달하게 되는데 그 정보를 파라미터라고 함 
- 서버에 파라미터 전송방법
    - 파라미터 전송 방법은 url에 ? 뒤에 파라미터=값&파라미터2=값 으로 전송
        - 사이트에 따라서 잘못된 접속으로 인지하고 에러처리할 수 있음
    - 파라미터를 dict로 구성해서 get(params=dict)


- https://sports.news.naver.com/news?oid=477&aid=0000312064
- params = {'param1': 'value1', 'param2': 'value'}
- res = requests.get(URL, params=params)

#### 문서에서 원하는 내용 추출하기(파싱)  
- html 문서에서 원하는 내용 추출
    - 필요한 내용만 추출
    - BeautifulSoup 라이브러리 사용
        - 태그 형식으로 된 text를 파싱할 때 사용
    - find() / findAll() 등 함수 사용

#### BeautifulSoup
- import bs4
- 데이터를 추출하는데 필요한 기능이 들어 있는 라이브러리 (파싱 라이브러리)
- 외부 라이브러리 : 설치해야 함
- 주피터는 기본 패키지임(설치하지 않아도 됨)
- 파이참 설치방법
    - File/Settings
    - Project Interpreter에서 bs4 검색
    - [Install Package]

#### BeautifulSoup 패키지의 파싱 함수
- find(태그,[{속성명:속성값}])
    - 지정한 태그 중 첫번째 만나는 태그만 추출 또는 지정한 태그 중 해당 속성과 속상값을 갖고있는 태그의 첫번째 태그
- findAll(태그,[{속성명:속성값}])
    - 지정한 태그 모두 찾아서 추출
    - 첫번째 이외의 태그를 추출할 때 사용
    - list 형태로 반환
- find_all(태그,[{속성명:속성값}])
    - findAll 함수와 동일

#### 웹 크롤링 시 주의 사항
- 웹 사이트는 언제든지 변경 될 수 있기 때문에 지금 실행하는 코드가 실행되지 않을 수 있다


#### 자동화 봇으로 보고 연결 끊는 경우 해결방법
- 서버에 요청시 header를 구성해 추가해 줌 즉, bot이 아님을 증명
- header 확인
    - 브라우저에서 해당 사이트 접속 시 생성하는 헤더를 개발자 도구로 확인(브라우저 정보 : User-Agent)
```python
url = df_menu['link'][2]
headers = {"User-Agent" : "header 넣기"}
res = requests.get(url, headers=headers)
```

#### urlopen SSL 에러
- 요청시 SSL 에러가 발생하면 보안연결을 시도해야 함
- import ssl 패키지를 사용
- ssl 연결 context()를 생성해서 context를 인수로 전달해야 함
```python
# [SSL: CERTIFICATE_VERIFY_FAILED]
import ssl
context = ssl._create_unverified_context()
url = 'https://jolse.com/category/toners-mists/1019/'
htmls = urlopen(url, context=context)
htmls = htmls.read()
```