T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}', end=' ')
    third = round((N ** (1/3)), 2)
    if third % 1 == 0:
        print(int(third))
    else:
        print(-1)

        
