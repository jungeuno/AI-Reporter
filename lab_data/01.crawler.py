from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl

context = ssl._create_unverified_context()
headers = {'User-Agent': 'Mozilla/5.0'}

url = 'https://news.naver.com/'
request = Request(url, headers=headers)                # 요청/ 코드에서 앞의 headers는 옵션
response = urlopen(request, context=context)           # 요청의 응답을 받음
html = response.read()                                 # 우클릭해서 소스보기/검사 한 html 코드를 변수에 저장

soup = BeautifulSoup(html, 'html.parser')              # 데이터 파싱/ 구조화 시켜서 저장
result = soup.find_all('div', {'class', 'cjs_t'})      # 전부 찾기/ 그냥 find는 발견된 첫번째 하나만 찾아줌

titles = []

for r in result:
    print(r.text)                                      # r.text는 태그안의 알맹이만 보여줌
    titles.append(r.text)                              # 컴퓨터가 관리하기 좋게 배열에 추가하여 정리

print(titles)