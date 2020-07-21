# 1번 문제
'''
import keyword
print(keyword.kwlist)
'''

# 2번 문제
'''
import math

num1 = 0.1 * 3
num2 = 0.3

print(math.isclose(num1, num2))
'''

# 3번 문제
'''
print('\n') # 줄 바꿈
print('\t') # 탭
print('\\') # 역슬래시 입력
'''

# 4번 문제
'''
name = input('이름을 입력하세요:')
print(f'안녕 {name}야!')
'''

# 5번 문제 오류 발생 코드 찾기(skip)

# 6번 문제
'''
n = 5
m = 9
print(('*' * n + '\n') * m)
'''

# 7번 문제
'''
print('\"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다.\"\n나는 생각했다.\'cd를 써서 git bash로 들어가 봐야지.\'')
'''

# 8번 문제
'''
A = input('이차항의 계수:')
B = input('일차항의 계수:')
C = input('상수항의 계수:')
a = int(A)
b = int(B)
c = int(C)
D = ((b**2) - 4 * a * c) 
if D > 0:
    answer1 = (-b + ((b**2) - 4 * a * c)**0.5) / (2 * a)
    answer2 = (-b - ((b**2) - 4 * a * c)**0.5) / (2 * a)
    print(f'근은 {answer1}, {answer2}입니다.')
elif D == 0:
    common_answer = (-b + ((b**2) - 4 * a * c)**0.5) / (2 * a)
    print(f'중근은 {common_answer}입니다.')
else:
	print('실근이 존재하지 않습니다.')
'''

# Workshop 1
'''
number = int(input('숫자를 입력하세요: '))
for i in range(1, number+1):
    print(i)
'''

# Workshop 2
'''
number = int(input('숫자를 입력하세요: '))

for i in range(1, number + 1):
    print(i, end=' ')
'''

# Workshop 3
'''
number = int(input('숫자를 입력하세요: '))
for i in range(number, -1, -1):
    print(i)
'''

#Workshop 4
'''
number = int(input('숫자를 입력하세요: '))

for i in range(number, -1, -1):
    print(i, end=' ')
'''

#Workshop 5
'''
number = int(input('숫자를 입력하세요: '))
j = 0
for i in range(1, number + 1):
    j += i

print(j)
'''
