num = int(input())

ls = list(map(int, input().split()))

#1
evens = 0
for i in range(0, num):
    if ls[i] % 2 == 0:
        evens += 1
print(f'짝수의 개수는 {evens}개 입니다.')

#2

for i in range(1, num):
    bigs = 0
    for j in range(0, num):
        if ls[i - 1] < ls[j]:
            bigs += 1
    print(f'A{i}보다 큰 숫자의 개수는 {bigs}개 입니다.')

#3

for i in  range(1, num):
    




