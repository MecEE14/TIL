# README

> pjt02의 README.MD입니다.

#### Problem_a.py

```python
import requests
from kobis import URLMaker


# 영화인상세정보 : people/searchPeopleInfo.json
# 영화인목록 : people/searchPeopleList.json
# 영화목록 : movie/serchMovieList
# 영화상세정보 : movie/serchMovieInfo

def filmo_count(people, movie):
    person = URLMaker()
    person_URL = person.get_url('people', 'searchPeopleList')# + f'&peopleNm={people}' + f'&filmoNames={movie}'
    feature = {
        'peopleNm' : people,
        'filmoNames' : movie
    }
    response = requests.get(person_URL, params=feature)
    dic = response.json()
    filmo = dic.get('peopleListResult').get('peopleList')[0].get('filmoNames')
    result = filmo.count('|') + 1
    #return result
    return len(filmo.split('|'))

    

if __name__ == '__main__':
    # 배우 이름과 작품을 이용하여 총 해당 배우가 몇 작품에 출연했는지 출력합니다.
    print(filmo_count('다우니', '아이언맨'))
```



### Problem_b.py

``` python
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
```



### Problem_c.py

```python
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
```



### Problem_d.py

```python
import requests

def naver(q1):
    url = 'https://openapi.naver.com/v1/search/movie.json'
    params = {
        'query': q1
    }
    PW = {
        'X-Naver-Client-ID': 'mXpwIuU83J7osDCpSu6f',
        'X-Naver-Client-Secret': '4XJnKGdo9X'
    }
    response = requests.get(url, params=params, headers=PW)
    result = response.json()
    print(result)

if __name__ == '__main__':
    naver('아이언맨')
```



### 배운점

- requests.get()은 url 외에도 params,  headers, cookies 등의 매개 변수가 있다.
  - 각 매개 변수는 설정하지 않으면 없음 값으로 입력됨.
- str 타입의 데이터에 .json()을 붙이면 딕셔너리화 할 수 있다.



### 느낀점

- 파이썬 문법을 배울때와 다르게 requests를 import해서 작업을 진행하는것은 매우 복잡하였다.
- requests 말고도 수많은 모듈들을 접할 생각을 하니 벌써 머리가 아픈것 같기도 하다.
- 오픈 api로 많은 정보들을 공유하지만, 사용법에 대해선 자세히 알려주고있는것 같지는 않다.

