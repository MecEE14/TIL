import requests
from kobis import URLMaker
from problem_b import get_movie_cd


def search_movie_info(movie_cd):
    person = URLMaker()
    person_URL = person.get_url('movie', 'searchMovieInfo')
    feature = {
        'movieCd' : movie_cd
    }
    response = requests.get(person_URL, params=feature)
    dic = response.json()
    movieinfo = dic['movieInfoResult']['movieInfo']
    movieNm = movieinfo['movieNm']
    openDt = movieinfo['openDt']
    genres = movieinfo['genres'][0]['genreNm']
    actors = movieinfo['actors'][0]['peopleNm']
    result = {
        'movieNm': movieNm,
        'openDt': openDt,
        'genres': [genres],
        'actors': actors
    }
    return result


if __name__ == '__main__':
    # 영화이름과 감독을 기준으로 영화코드를 검색하여 변수 movie_cd에 저장합니다.
    movie_cd = get_movie_cd('기생충', '봉준호')
    # movie_cd를 이용하여 상세정보를 조회하여 출력합니다.
    print(search_movie_info(movie_cd))
