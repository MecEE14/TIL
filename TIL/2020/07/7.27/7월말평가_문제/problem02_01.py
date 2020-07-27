import json

def check(data):
    result = []                                 # 빈 리스트 생성
    
    for i in data:                              # 리스트 속의 리스트들을 하나의 리스트로 만듦
        result += [i[0]] + [i[1]]
    ln = len(result)                            # 리스트의 길이 확인
    for j in range(0, ln - 2):                  # 3번 연속으로 37.5도 이상의 값이 있는지 확인 
        if result[j] >= 37.5 and result[j+1] >= 37.5 and result[j + 2] >= 37.5:
            ch = True
        else:
            ch = False
    return ch                                   # 참/거짓 반환


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperature_json = open('problem02_data.json', encoding='UTF8')
    temperature_list = json.load(temperature_json)
    print(check(temperature_list))
    # => True