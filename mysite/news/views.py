from django.shortcuts import render
from news.models import Article
from news.vg_scraper import scraper
# Create your views here.


def header(request):
    return render(request, 'news_header.html')

def update(request):
    out = scraper()
    for i in out:
        foo = Article.objects.create(image_title = i[0],
                                     image_text = i[1],
                                     title = i[2],
                                     ingress = i[3],
                                     hoveddel = i[4])
    return render(request, 'news_header.html')