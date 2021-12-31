from django.shortcuts import render
from . import all_news
from datetime import date
from .models import news_details
Date =date.today().strftime("%d %b %Y")


def index(request):
    newss = all_news.all_news()
    for news in newss:
        title = news['title']
        img_url = news['urlToImage']
        date = news['publishedAt']
        source = news['source']['name']

        data = news_details(title=title,img_url=img_url,date=date,source=source)
        data.save()
    return render(request,"index.html",{'newss': newss, "date": Date})
