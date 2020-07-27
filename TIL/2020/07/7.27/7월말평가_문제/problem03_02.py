def caesar(word, n):
    result = ''                         # 빈 문자열 생성
    for i in word:
        num = ord(i)                    # 각각의 문자를 아스키코드 값으로 변환
        if 65 <= num <= 90:             # 문자가 대문자일 때
            if num + n > 90:            # 밀린 값이 대문자 Z의 값을 넘으면
                num += n -26            # A부터 다시 시작하게함
                result += chr(num)      # 아스키코드값을 문자로 재변환하여 문자열에 추가
            else:
                num += n                # 넘지 않을 때
                result += chr(num)
        else:
            if num + n > 123:           # 문자가 소문자일 때
                num += n -26            # 밀린 값이 소문자 z의 값을 넘으면 a부터 다시 시작하게함
                result += chr(num)      # 아스키코드값을 문자로 재변환하여 문자열에 추가
            else:
                num += n                # 넘지 않을 때
                result += chr(num)
    return result                       # 최종 문자열 반환

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # => 'fuuqj'
    print(caesar('ssafy', 1))
    # => 'ttbgz'
    print(caesar('Python', 10))
    # => 'Zidryx'