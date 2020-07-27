import json

def rotate(data):
    am = []                     # 빈 리스트 작성
    pm = []
    for temp in data:           
        am += [temp[0]]         # 각각의 리스트에 해당하는 값을 리스트 형태로 추가
        pm += [temp[1]]
    result = {                  # 딕셔너리 생성
        'am': am,               # 키와 밸류를 집어넣음
        'pm': pm
        }
    return result               # 결과 반환

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperature_json = open('problem02_data.json', encoding='UTF8')
    temperature_list = json.load(temperature_json)
    print(rotate(temperature_list))
    # => {
    #     'am': [36.7, 36.9, 37.8, 36.7, 36.3, 36.5, 36.8], 
    #     'pm': [36.5, 37.5, 37.8, 36.5, 36.4, 36.5, 36.6]
    # }
