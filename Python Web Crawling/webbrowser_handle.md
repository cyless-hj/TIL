- 웹 크롤링은 웹 브라우저를 통해 진행 됨
    - 웹 브라우저를 컨트롤 할 수 있어야 함
    - 관련 패키지 : webbroswer

### 브라우저 실행 : webbrowser.open('url')

- 매개변수 : url을 전달(접속하고자 하는 웹 사이트)
    - url은 파라미터를 포함 할 수 있음
    - ex) https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=python
    - ? 를 기준으로 왼쪽은 서버 주소(기본 url), 오른쪽은 파라미터
    - https://search.naver.com/search.naver? - 검색을 위한 필수 주소
    - where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=python - 서버에 전달되는 파라미터(query = 검색어)
- 반환값이 True면 브라우저 실행이 정상 완료

### 단, 검색어를 url에 적용시키는 방법은 site마다 다르다
- 구글 검색 URL
    - https://www.google.com/search?q=python&oq=python&aqs=chrome..69i57j69i59l3j0i131i433i512l6.1997j0j15&sourceid=chrome&ie=UTF-8
    - 기본 url : https://www.google.com/search?
    - 검색 파라미터 : q=검색어