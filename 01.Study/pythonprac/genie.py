import requests # requests 라이브러리 설치 필요
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# print(soup)
#body-content > div.newest-list
songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for song in songs:
    rank = song.select_one('td.number').text[0:2].strip()
    title = song.select_one('td.info > a.title.ellipsis').text.strip()
    singer = song.select_one('td.info > a.artist.ellipsis').text.strip()
    print(rank, title, singer)