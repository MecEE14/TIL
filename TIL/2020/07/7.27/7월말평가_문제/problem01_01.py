import json

def over(movie):
    num = movie['user_rating'] # 평점을 변수화
    if num >= 8:               # 변수화한 평점과 기준의 비교
        result = True
    else:
        result = False
    return result              # 참/거짓 값 반환


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem01_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(over(movie)) 
    # => True