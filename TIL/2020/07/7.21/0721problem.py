'''
students = ['김철수', '김영희', '김가영']
print(len(students))
'''
'''
word = input()
# 아래에 코드를 작성하시오.
a = list(word)
'''
'''
word = input()
b = list(word)
l = range(len(b) - 1, -1, -1)
for i in l:
    print(b[i])
'''
'''
work = input()
result = ''
for char in work:
    result = char + result
print(result)
'''


'''
    number = int(input())
numbers = list(range(1, number + 1))
A = 0
B = 0
if number > 30:
    print('30 이하의 자연수를 써 주세요.')
else:
    a_number = list(range(1, number + 1, 2))
    b_number = list(range(2, number + 1, 2))
    for i in a_number:
        A += (i * 2)
        
    for j in b_number:
        B += (j * 3)
    print(A + B)
'''
'''
number = int(input())
prime = list(range(2, number))
a = 'Y'
if 2 <= number <= 1000:
    for i in prime:
        if number % i != 0:
            i += 1
        else:
            a = 'N'
    print(a)
else:
    print('2 이상 1000 이하의 정수를 입력해주세요.')
'''
'''
number = int(input())

is_prime = 'Y'
for i in range(2, number):
    if number % i == 0:
        is_prime = ('N')
print(is_prime)
'''
'''
number = [26, 39, 51, 53, 57, 79, 85]
j = 0
num = number[j]
i = 2
while j != 7:
    while(i != number[j] + 1):
        if number[j] % i != 0:
            i += 1
        else:
            if number[j] != i:
                print(f'{number[j]}은(는) 소수가 아닙니다. {i}은(는) {number[j]}의 인수입니다.')
                i = number[j] + 1
            else:
                print(f'{number[j]}은(는) 소수입니다.')
                i = number[j] + 1
    i = 2
    j += 1
'''