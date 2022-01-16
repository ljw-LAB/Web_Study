# print('hello sparta!')
# a = 'jae'
# b = 'lee'
# a_list = ['사과', '배', '감']
# a_list.append('수박')
# print(a_list)

# a_dict = {
#     'name' : 'bob',
#     'age' : 27
# }
#
# print(a_dict['name'])

# def sum(a, b):
#     print('더하자!')
#     return a+b
#
# result = sum(1,2)
# print(result)

# def is_adult(age):
#     if age > 20 :
#         print('성인입니다')
#     else :
#         print('청소년입니다')
#
# is_adult(15)

# fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']
#
# count = 0
#
# for fruit in fruits:
#     if fruit == '배':
#         count += 1
# print(count)

# people = [{'name': 'bob', 'age': 20},
# {'name': 'carry', 'age': 38},
# {'name': 'john', 'age': 7},
# {'name': 'smith', 'age': 17},
# {'name': 'ben', 'age': 27}]
#
# for person in people :
#     if person['age'] > 20:
#         print(person)

# import requests # requests 라이브러리 설치 필요
#
# r = requests.get('http://spartacodingclub.shop/sparta_api/seoulair')
# rjson = r.json()
#
# rows = rjson['RealtimeCityAir']['row']
#
# # print(rows)
#
# for row in rows :
#     # print(row)
#     gu_name = row['MSRSTE_NM']
#     gu_mise = row['IDEX_MVL']
#     # print(gu_name, gu_mise)
#     if gu_mise < 60 :
#         print(gu_name)

import requests # requests 라이브러리 설치 필요
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.sunnb.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# print(soup)
# 코딩 시작

# title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
# print(title.text)
# print(title['href'])

movies = soup.select('#old_content > table > tbody > tr')
#
# # print(movies)
#
for movie in movies :
    a = movie.select_one('td.title > div > a')
    b = movie.select_one('td:nth-child(1) > img')
    c = movie.select_one('td.point')
    # old_content > table > tbody > tr:nth-child(2) > td:nth-child(1) > img
    # old_content > table > tbody > tr:nth-child(2) > td.point
    # print(a)
    # print(a.text)
    # if a is not None:
    #     title = a.text
    #     rank = movie.select_one('td:nth-child(1) > img')['alt']
    #     star = movie.select_one('td.point').text
    #     print(title, rank, star)
    if a is not None:
        title = a.text
        rank = b['alt']
        star = c.text
        print(rank, title, star)
        doc = {
            'title': title,
            'rank': rank,
            'star': star
        }
        db.movies.insert_one(doc)
