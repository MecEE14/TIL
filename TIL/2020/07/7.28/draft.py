T = int(input())
for test_case in range (1, T + 1):
    N, K = map(int, input().split())
    final_score = []
    fg = ''
    for i in range(1, N + 1):
        score = list(map(int, input().split()))
        final_score += [((score[0] * 0.35) + (score[1] * 0.45) + (score[2] * 0.2)) / 3]
    person = final_score[K - 1]
    final_score.sort()
    for j in range (0, N):
        if person == final_score[j]:
            grade = j + 1
    if grade > 9 * float(N) / 10:
        fg = 'A+'
    elif grade > 8 * float(N) / 10:
        fg = 'A0'
    elif grade > 7 * float(N) / 10:
        fg = 'A-'
    elif grade > 6 * float(N) / 10:
        fg = 'B+'
    elif grade > 5 * float(N) / 10:
        fg = 'B0'
    elif grade > 4 * float(N) / 10:
        fg = 'B-'
    elif grade > 3 * float(N) / 10:
        fg = 'C+'
    elif grade > 2 * float(N) / 10:
        fg = 'C0'   
    elif grade > 1 * float(N) / 10:
        fg = 'C-'
    else:
        fg = 'D0'
    print(f'#{test_case}', end=' ')
    print(f'{fg}')

