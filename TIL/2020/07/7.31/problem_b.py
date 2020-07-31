import requests
from kobis import URLMaker


def get_movie_cd(title, director):
    person = URLMaker()
    person_URL = person.get_url('movie', 'searchMovieList')
    feature = {
        'movieNm' : title,
        'directorNm' : director
    }
    try:

        response = requests.get(person_URL, params=feature)
        dic = response.json()
        result = dic.get('movieListResult').get('movieList')[0].get('movieCd')
        return result
    except:
        return 0


if __name__ == '__main__':
    # 영화이름과 감독을 기준으로 영화코드를 검색합니다.
    print(get_movie_cd('기생충', '봉준호'))