# GIMME BACK MY STRONGLY TYPED JAVA MOM GIVE IT BACKKKKKKKKKKK
import datetime
import csv
import bs4
import requests
from bs4 import BeautifulSoup, SoupStrainer

db = open(datetime.datetime.now().strftime("%Y:%m:%d-%H:%M")+ ".csv", 'w')
fieldnames = ["url", "time", "title", "deck"]


file = open(datetime.datetime.now().strftime("%Y:%m:%d-%H:%M")+ ".md", 'a')
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
            souptime = BeautifulSoup(document, "html.parser", parse_only=SoupStrainer("time", attrs={"class": "timeStamp"}))

            title = souph1.find("h1", class_="detailHeadline")
            deck = souph2.find("h2", class_="deck")
            time = souptime.find("time", class_="timeStamp")
            if title:
                ans[link] = [title.text.strip(),deck.text.strip(), time.text.strip()]
    return ans

def generateMD(dict):
    for i in dict:
        file.write("# " + dict[i][0] + "\n")
        file.write(f"{dict[i][2]}\n"
                   f"{i}\n"
                   f"{dict[i][1]}\n")
    file.close()

def saveToCsv(dict):
    csvwriter = csv.writer(db, delimiter=",", quotechar='"')
    for i in dict:
        csvwriter.writerow([i, dict[i][2], dict[i][0], dict[i][1]])

dict = recursiveGet(getNews("https://www.cbc.ca/news"),"https://www.cbc.ca/news")

saveToCsv(dict)
generateMD(dict)

