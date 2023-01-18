from django.shortcuts import render
from news.models import News


def index(request):
    template = 'news/index.html'
    articles_list = News.objects.all()

    context = {
        'articles_list': articles_list
    }
    

    return render(request, template)