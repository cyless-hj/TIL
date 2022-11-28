## Oracle Cloud DB - Django 연동
- Django app settings.py Database에 다음과 같은 형식으로 작성
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '', # tnsname
        'USER': '', # userID
        'PASSWORD': '' # userPW
    }
}
```
- cx_Oracle 설치
- Oracle Instant Client 설치
- Oracle Instant Client Path 설정
- Oracle Instant Client 내 network/admin 안에 DB Wallet sqlnet.ora, tnsnames.ora 파일 추가
- sqlnet.ora 수정 : Directory 현재 Oracle Instant Client\network\admin으로 변경
```python
python manage.py inspectdb test>MZ_recommend_system/models.py
```
- model.py 생성