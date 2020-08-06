T = int(input())

for tc in range(1, T + 1):
    cnt = 0
    P, A, B = map(int, input().split())
    def find(p, t, s = 1):
        global cnt
        m = int((p + s) / 2)
        if m == t:
            cnt += 1
            return cnt
        elif m > t:
            p = m
            cnt += 1
            return find(p, t, s)
        elif m < t:
            s = m
            cnt += 1
            return find(p, t, s)
    a = find(P, A)
    cnt = 0
    b = find(P, B)

    if a < b:
        print(f'#{tc} A')
    elif a > b:
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')







    