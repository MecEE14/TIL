T = int(input())
for t in range(1, T + 1):
    u, a, b = map(int, input().split())
    max_num = 0
    min_num = 0
    c = abs(a + b)
    if u < c:
        min_num = c - u
    if a < b:
        max_num = a
    else:
        max_num = b
    print(f'#{t} {max_num} {min_num}')