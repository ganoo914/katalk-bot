import requests
from bs4 import BeautifulSoup
import datetime

# 1) \requsts 라이브러리를 활용한 HTML 페이지 요청
# 1-1) res 객체에 HTML 데이터가 저장되고, res.content로 데이터를 추출
res = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=blBI&pkid=682&os=24930746&qvt=0&query=%EC%96%91%EC%96%91%EA%B3%A0%EB%93%B1%ED%95%99%EA%B5%90%20%EA%B8%89%EC%8B%9D%EC%8B%9D%EB%8B%A8")

# print(res.content)
# 2) HTML 페이지 파싱 BeautifulSoup (HTML 데이터, 파싱방법)
# 2-1) BeautifulSoup 파싱방법
soup = BeautifulSoup(res.content, "html.parser")

# 3) 필요한 데이터 검색
# title_1 = soup.find('div',class_="time_normal_list")
# title_2 = soup.find_all('div', {"class" : "timeline_box"})
# title_2 = soup.find('div', {"class" : "timeline_box"})
# title_2_a = title_1.find_all('li')
# title = soup.find('strong', class_="cm_date")

title = soup.find('div', {"class" : "timeline_list open"})

# 4) 필요한 데이터 추출
# print(title.get_text())

lim = title.get_text().split()
time_ = []
# print(title.get_text())
# print(title.get_text())
# 유사도 -> 엑셀 ------------- 

print(lim)
lim.insert(-1,"아침")

d1,d2=0,0
for i in enumerate(lim):
    if i[1]=="아침":
        d1=d2
        d2=i[0]
        time_.append(lim[d1-1:d2-1])
print(time_, "\n")
