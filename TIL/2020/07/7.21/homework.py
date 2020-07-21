# 1. Mutable & Immutable
'''
String, List, 
Tuple, Range, Set, Dictionary
'''

# 2. 홀수만 담기
'''
num = range(1,51)
number = list(num[0:50:2])
print(number)
'''
# 3. Dictionay 만들기
'''
our = range(1, 25)
for i in our:
    Aclass = {'i', i}
    print(Aclass)
'''
'''
Aclass = {'강해성': 1, '곽민준': 2, '구본혁': 3, '기예림': 4, '김경윤': 5, '김현지': 6, '박예린': 7, '백은경': 8, '신상훈': 9, '오민택': 10, '오진영': 11, '우진하': 12, '이대련': 13, '이도건': 14, '이민정': 15, '이송영': 16, '이형창': 17, '이호창': 18, '전영제': 19, '전원표': 20, '조단원': 21, '조성국': 22, '최재영': 23, '황윤호': 24 }
print(Aclass)
'''
# 4. 반복문으로 네모 출력
'''
n = 5
m = 9

for i in range(1, m+1):
    print('*' * n)
'''

# 5. 조건 표현식
'''
temp = 36.5
print('입실 불가') if temp >=37.5 else print('입실가능')
'''
# 6. 평균 구하기
'''
j = 0
scores = [80, 89, 99, 83]
for i in scores:
    j += i
print(j/4)
'''



