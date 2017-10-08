#-*- coding:utf-8 -*-
import csv
from urlparse import urljoin
from bs4 import BeautifulSoup
import requests


url = "https://movie.douban.com/top250?start={startpage}&filter="
startpage = 0
page = 0
csv_file = open("/home/wilhelm/Python练习/Python/Top_250.csv","wb")
csv_writer = csv.writer(csv_file,delimiter=',')

while True:
    page +=1
    print "fetch:", url.format(startpage = startpage)
    response = requests.get(url.format(startpage=startpage))
    html = BeautifulSoup(response.text)
    movie_list = html.select(".grid_view > li")
    startpage +=25
    if startpage > 250:
        break

    for movie in movie_list:
        movie_url = movie.select("a")[0]["href"]
        #movie_url1 = movie.select(".hd")[0].select("a")[0]["href"]
        movie_title_eng = movie.select(".hd")[0].select("a")[0].select("span:nth-of-type(2)")[0].string.encode("utf8")
        movie_title = movie.select(".hd")[0].select("a")[0].select(".title")[0].string.encode("utf8")
        movie_title_other = movie.select(".hd")[0].select("a")[0].select(".other")[0].string.encode("utf8")
        movie_score = movie.select(".star")[0].select(".rating_num")[0].string.encode("utf8")
        movie_people = movie.select(".star")[0].select("span:nth-of-type(4)")[0].string.encode("utf8")
        #comment = movie.select(".quote")[0].select(".inq")[0].string.encode("utf8")
        if movie.select(".quote"):
            movie_comment = movie.select(".quote")[0].select(".inq")[0].string.encode("utf8")
        else:
            movie_comment = None
        movie_rank = movie.select("em")[0].string.encode("utf8")
        movie_year = movie.select(".bd")[0].select("p")[0]
        
        csv_writer.writerow([movie_title,movie_rank,movie_score,movie_people,movie_comment,movie_url])

csv_file.close()


    
    
    
