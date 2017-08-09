from django.shortcuts import render

# Create your views here.


def header(request):
    return render(request, 'news_header.html')