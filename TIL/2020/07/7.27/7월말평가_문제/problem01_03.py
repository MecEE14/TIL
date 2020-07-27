import json

def history(movie):
    sto = movie['overview']             # 줄거리 키를 가지고 밸류 가져옴
    ex = sto.find('과거')               # 줄거리 밸류에 '과거'라는 단어가 있는지 찾음
    if ex == -1:                        # 참/거짓 확인
        result = False
    else:
        result = True
    return result                       # 참/거짓 반환

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem01_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(history(movie)) 
    # => False