def swap(word):
    result =''                      # 빈 문자열 생성
    for i in word:                  # 각각의 아스키코드 값 확인
        num = ord(i)
        if num >= 91:               # 소문자일 경우 대문자로 변환
            num -= 32
            result += chr(num)      # 문자의 형태로 변환하여 추가
        else:                       # 대문자일 경우 소문자로 변환
            num += 32
            result += chr(num)
    return result                   # 문자의 형태로 변환하여 추가

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(swap('aPpLe'))
    # => 'ApPlE'
    print(swap('SSAFY'))
    # => 'ssafy'
    print(swap('Python'))
    # => 'pYTHON'