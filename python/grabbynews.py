# GIMME BACK MY STRONGLY TYPED JAVA MOM GIVE IT BACKKKKKKKKKKK
import datetime

import bs4
import requests
from bs4 import BeautifulSoup, SoupStrainer


file = open(datetime.datetime.now().strftime("%H:%M")+ ".md", 'a')
newsBase=["https://www.cbc.ca/news", "https://ground.news/"]

def getNews(link):
    news = []
    ans = []
    document = requests.get(link).text
    soup = bs4.BeautifulSoup(document, "html.parser", parse_only=SoupStrainer("a"))

    for url in soup :
        if url.has_attr("href"):
            news.append(url["href"])

    if link == "https://www.cbc.ca/news":

        blacklist=['/news/local',
                   '/news/climate',
                   '/news/world',
                   '/news/canada',
                   '/news/politics',
                   '/news/indigenous',
                   '/news/opinion',
                   '/news/thenational',
                   '/news/business',
                   '/news/health',
                   '/news/entertainment',
                   '/news/science',
                   '/news/investigates',
                   '/news/gopublic',
                   '/news/about-cbc-news-1.1294364', ]

        news = list(set(news) - set(blacklist))

        for item in news:
            if item.startswith("/news/") | item.startswith("/sports/"):
                ans.append(item)
            else:
                pass
    return ans

def recursiveGet(new, url):
    ans ={}
    for i in new:
        if url == "https://www.cbc.ca/news":
            link = "https://www.cbc.ca"+i
            document = requests.get(link).text
            souph1 = BeautifulSoup(document, "html.parser", parse_only=SoupStrainer("h1", attrs={"class":"detailHeadline"})) # Intended, add/remove as you need
            souph2 = BeautifulSoup(document, "html.parser", parse_only=SoupStrainer("h2", attrs={"class": "deck"}))
            time = BeautifulSoup(document, "html.parser", parse_only=SoupStrainer("h2", attrs={"class": "deck"}))

            title = souph1.find("h1", class_="detailHeadline")
            deck = souph2.find("h2", class_="deck")
            time = time.find("time", class_="timeStamp")
            if title:
                ans[link] = [title.text.strip(),deck.text.strip(), time.text.strip()]
    return ans
news = getNews("https://www.cbc.ca/news")

def generateMD(dict):
    for i in dict:
        file.write("# " + dict[i][0] + "\n")
        file.write(dict[i][2]+"\n"+i+"\n"+dict[i][1]+"\n")
    file.close()

generateMD(recursiveGet(getNews("https://www.cbc.ca/news"),"https://www.cbc.ca/news"))


