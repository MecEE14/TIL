# 아래에 코드를 작성하세요.

# 1. 필요한 모듈을 불러오세요.
import requests
import bs4

name = input('아이디를 입력하세요 : ')

url = 'https://www.op.gg/summoner/userName='+ name # 우리가 원하는 정보를 가지고 있는 페이지  
print(url)
# 2. requests 모듈로 요청을 보내세요.
response = requests.get(url).text # HTML 문서를 Text 형태로 응답받아옴
selector = '#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierRank'           # 우리가 원하는 정보를 가지고 있는 요소의 선택자

# 3. bs4 모듈로 데이터를 가져오세요.
# HTML 문자 덩어리를 해석해서 선택자를 통해 접근할 수 있도록 만들어줌
data = bs4.BeautifulSoup(response, 'html.parser')
result = data.select_one(selector)

print(f'그래서 님의 티어는 {result.text} 이군.')