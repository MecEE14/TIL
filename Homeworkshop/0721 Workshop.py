# 1번 문제
'''
N = int(input('자연수를 입력하세요. : '))
if 1000 >= N >= 1:
    for i in range(1, N+1):
        if N % i == 0:
            print(i, end=' ')
else:
    print("0부터 1000사이의 자연수만 입력하세요")
'''

# 2번 문제
'''
number = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]
number.sort()
print(number[17])
'''

# 3번 문제
'''
num = int(input('자연수를 입력하세요 : '))
#nums = range(1, num + 1)
j = 1
for i in range(1, num+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print('')
'''

# 4번 문제
'''
j = 1
for i in range(2, 10):
    print(f'------- [{i} 단] -------')
    for j in range(1, 10):
        print(f'{i} X {j} = {i*j}')
    '''

