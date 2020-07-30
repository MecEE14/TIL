T = int(input())

for test in range(1, T + 1):
    a, b, A, B = map(int, input().split())
    hour = a + A
    mint = b + B
    if mint >= 60:
        hour += 1
        mint -= 60
    if hour >= 13:
        hour -= 12
    print(f'#{test} {hour} {mint}')