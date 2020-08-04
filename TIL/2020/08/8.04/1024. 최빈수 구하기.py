T = int(input())
for t in range(1, T + 1):
    n = int(input())
    scores = list(map(int, input().split()))
    max_count = 0
    score = 0
    for i in range(1, 101):
        cs = scores.count(i)
        if cs > max_count:
            score = i
            max_count = cs
        elif cs == max_count:
            if score < i:
                score = i
    print(f'#{n} {score}')
        
            