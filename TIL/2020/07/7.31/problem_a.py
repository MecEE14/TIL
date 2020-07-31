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