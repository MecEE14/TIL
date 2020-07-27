import json

def title_length(movie):
    name = movie['title']                   # 제목을 가져옴
    ln = len(name)                          # 제목의 길이 측정
    result = f'영화 제목은 {ln}글자 입니다.'  
    print(result)
    return ln                               # 제목의 길이 반환

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('problem01_data.json', encoding='UTF8')
    movie = json.load(movie_json)
    print(title_length(movie)) 
    # => 4