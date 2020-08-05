data = [-7, -3, -2, 5, 8]

n = len(data)
ls = []
result = 0
for i in range(1<<n):
    temp = []
    temp_sum = 0
    for j in range(n + 1):
        T = i & (1<<j)
        if i & (1<<j):
            temp += [data[j]]
        for k in temp:
            temp_sum += k
    if temp_sum == 0:
        result += 1
    ls += [temp]
print(result)

