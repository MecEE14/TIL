# Homework
# prob 1
'''
int, float, str, list, dict, complex
'''

# prob 2
'''
__init__ : 인스턴스 객체가 생성될 때 호출되는 함수
__del__ : 인스턴스 객체가 소멸되기 직전에 호출되는 함수
__str__ : 특정 개체를 출력할 때 보여줄 내용을 정의할 수 있음
__repr__ : 사용자가 이해할 수 있는 객체의 모습을 표현
'''

# prob 3

'''
.replace(a, b) : 문자열에 포함된 a의 문자열을 b의 문자열로 치환
.append(c) : 리스트에 c값을 추가함
.update({'d': 1}) : 딕셔너리에 괄호 안의 값을 추가
'''

# prob 4
'''
from fibo import fibo_recursion as recursion

print(recursion(6))
'''

# Workshop
# prob 1
'''
(1) faker라는 이름의 깃허브의 파일에 접근할 수 있게 해줌
(2) 코드 파일이 만들어지는 폴더 안에서 git bash를 열어 실행
'''

# prob 2
'''
from faker import Faker # 1 faker라는 패키지에 선언된 Faker 함수만을 불러오는 코드이다.
fake = Faker()          # 2 Faker는 불러온 함수, fake는 Faker함수의 변수화(별명)
fake.name()             # 3 name()은 fake의 메서드이다.
'''

# prob 3
'''
class Faker():

    def __init__(self, country = 'en_US'):
        pass
    '''

# prob 4
'''
#1과 #2는 같은 값이 출력된다.
seed는 random 함수의 입력값에 해당하며, 입력하지 않을 경우 현재 시간을 seed로 사용한다.
seed가 같으면 출력값이 같다.
'''

# prob 5
'''
문제 4번에서 출력되는 값과 같은 값이 출력되며,
seed_instance()는 seed()와 같은 역할을 한다
'''