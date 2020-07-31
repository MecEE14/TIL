class URLMaker:
    
    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest'
    key = 'ae077aac11b828e973fe4f612f3f1b9c' # 나의 키


    def __init__(self, key = key):
        self.key = key


    def get_url(self, category='boxoffice', feature='searchWeeklyBoxOfficeList'):
        return f'{self.url}/{category}/{feature}.json?key={self.key}'
