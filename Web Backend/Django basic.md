# Django<br>

## 장고
- 파이썬 기반으로 작성된 오픈소스 웹 어플리케이션 프레임워크
    - 프레임워크 : 뼈대, 골조라고도 하며 프로그램을 개발하는 데에 있어서 사용되는 기본 개념 구조
- 즉, 파이썬 프로그래밍 언어를 기반으로 한 동적인 웹을 작성하는 데에 있어 장고라는 기본 개념 구조 요소를 이용하여 개발

## 장고의 특징
- 웹 개발에 있어서 번거로운 요소들을 새로 개발할 필요 없이 내장된 기능만을 이용해 빠른 개발을 할 수 있다는 장점
    - **MTV패턴 – M(Model),(Template) , V(View)**
    - **MVC패턴 – M(model),V(Template), C(Controller-views.py)**

## MVT 패턴
- Model + View + Template
- MTV 패턴이라고도 함
- 웹 어플리케이션을 개발하는 데에 있어서 영역을 크게 위의 3가지로 나눈 것
    - 독립적으로 개발
    - 3가지로 나누어서 개발을 하는 데에 있어서 딱히 정해진 순서는 없음

## Django 프로젝트
1. Django install
```
pip install django
```

2. Django app 시작

```python
python manage.py startapp my_to_do_app
```

3. Django migrate
- 마이그레이션(Migration)이란 데이터베이스의 스키마(Schema)를 관리하기 위한 방법
- 데이터베이스에 테이블, 필드 등의 변경이 발생했을 때 지정된 데이터베이스에 적용하는 과정을 의미
- 현재 모델(model.py)은 정의만 되어있을 뿐, 데이터베이스를 생성하고 적용하지 않았음
- 마이그레이션을 통해 데이터베이스를 생성하고 모델의 생성, 변경, 삭제 등에 따라 작업 내역을 관리하고 데이터베이스를 최신 화 할 수 있다

```python
python manage.py migrate
```
- 마이그레이션 진행 시, 장고 프로젝트에서 사용하는 11개의 기본 테이블이 생성됨<br>

- model.py에 정의된 모델의 생성/변경 내역을 히스토리 관리, 데이터베이스에 적용 등과 같은 기능을 제공하여 손쉽게 데이터베이스의 구조를 바꿀 수 있음
- 장고에서는 데이터베이스를 제공하고 있기 때문에 제공되는 데이터베이스(sqlite)를 사용할 수 있으며, 해당 db 에서 사용할 테이블 생성

4. Django 서버 실행
```python
python manage.py runserver
```

5. Django 디폴트페이지 확인

6. 프로젝트 환경설정
- 프로젝트에 포함되는 모든 app는 모두 설정파일에 등록해야 함

## DB 처리
- views.py에 .save() 메소드를 이용하여 저장

## model 관련 코딩
- models.py – 테이블 정의
- admins.py – 정의된 테이블이 admin 화면에 보이게 함
- manage.py makemigrations – 데이터베이스에 변경이 필요한 사항을 추출
- manage.py migrate – 데이터베이스에 변경사항을 반영
- manage.py runserver – 현재까지 작업 개발을 웹서버로 확인

## 모델 생성(DB 생성)
- models.py에 모델 객체 클래스를 생성한다.

## models.py에서 정의할 수 있는 데이터
- CharField : 문자열
- DateField : 날짜
- EmailField : e-mail => 
    - EmailValidator라는 것을 통해 입력되는 문자열이 이메일 형식인지를 자동 체크해 줌
    - 형식에서 어긋하면 저장과정에서 오류 발생
- FileField : 파일을 저장할 수 있는 데이터 타입
    - 파일의 이름을 저장하며 실제 파일은 upload_to라는 옵션에 지정되는 위치에 저장
- TextField : 글자수의 제한이 없음
- IntegerField : 숫자
- BooleanField : T/F

## DB에 반영
```python
python manage.py makemigrations
python manage.py migrate
```

## DB shell 확인
1. DB shell 열기
```python
python manage.py dbshell
```

2. Table 확인
```
.tables
```

3. Table 내용 확인
```
PRAGMA table_info(table_name);
select * from table_name;
```

## 저장 후 출력 FLOW
1. 사용자가 메모 입력 후 메모하기 클릭
2. 서버로 메모(todoContent)파라미터와 함께 서버에 요청
3. 서버는 해당 요청을 받은 후 http://127.0.0.1:8000/createTodo/ 의 url을 확인함
    1. path('createTodo/', views.createTodo, name='createTodo’),
    2. views.py의 createTodo 함수를 실행
    3. createTodo함수는 전송된 파라미터를 DB에 저장 후
    4. views.index는 DB에 있는 모든 메모를 갖고 와서 파라미터를 통해 template(index.html)에게 전달
    5. template은 전달된 파라미터로 동적 코드를 생성(rendering)
4. index.html코드 응답 반환: 위 모든 처리를 끝낸 후 index.html을 반환해야 함
    1. vews.index에서 처리 후 index.html 반환(이 처리를 편하게 하기 위해 redirect 기능을 이용함)

## { } 템플릿 태그
- {} : html에 파이썬 코드를 추가할 수 있는 태그
    - {% %} : 파이썬 문법
    - {{ }} : 사용자에게 직접 보여주는 값

## on_delete
- CASECADE
    - 외래키로 지정되어 참조되는 요소가 삭제되면 참조하는 모든 요소도 삭제 함
- SET_DEFAULT
    - 참조되는 요소가 삭제될 때 이를 참조하는 요소에 대해서 참조 값을 설정해 둔 DEFAULT 값으로 설정
- PROTECT
    - 참조되는 요소를 삭제하려고 할 때 해당요소를 참조하는 요소가 하나라도 존재한다면 에러를 발생
- SET_NULL
    - 참조되는 요소가 삭제될 때 이름 참조하는 요소에 대해서 참조 값을 NULL로 설정

## superuser 생성
```python
python manage.py createsuperuser
```

## 보안기능
- csrf_token
    - 올바르지 않은 방법으로 데이터가 전송되면 서버에서 발생된 csrf_token값과 해커가 보낸 csrf_token 값이 일치하지 않으므로 오류를 발생시켜 보안을 유지할 수 있다.
