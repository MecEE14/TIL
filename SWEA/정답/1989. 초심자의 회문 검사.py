T = int(input())

for test_case in range(1, T + 1):
    def pan(word):
        while len(word) > 2:
            if word[0] == word[-1]:
                word = word[1:-1]
                return pan(word)
            else:
                return 0
        return 1
            
    word = input()
    result = pan(word)
    print(f'#{test_case}', end=' ')
    print(f'{result}')
