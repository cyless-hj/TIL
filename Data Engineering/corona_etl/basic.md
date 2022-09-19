# 클래스
- 데이터 + 함수
- class method, static method
- instance method
- 클래스 이름은 길더라도 최대한 명확하게 작명 해주는 것이 좋다.

# 접근제한자
- public, protected,        private
-       , __메서드, 변수,    __메서드, __변수

# Refactoring
- 낮은 결합도, 높은 응집도를 위해 리팩토링을 진행한다.
- 디자인 패턴을 이용하여 진행할 수 있다.
- 변경의 가능성이 있는 부분은 메인 함수에서 나누어 따로 작성하는 것이 좋다.

# Enum
- 절대 변경될 일 없는 객체를 Enum객체로 생성한다.