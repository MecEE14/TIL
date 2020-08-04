T = int(input())
a, b = map(int, input().split())
ls = list(map(int,input().split()))
max_len = 0
for i in range(0, b):
    max_tem = 0
    for j in range(0, a):
        if ls[j] != 0:
            if max_tem > max_len:
                max_len = max_tem
                max_tem = 0
                ls[j] = ls[j] - 1
            else:
                max_tem = 0
                ls[j] = ls[j] -1
        else:
            max_tem += 1
print(max_len)