from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from news.models import News


@login_required
def index(request):
    template = 'news/index.html'
    articles_list = News.objects.all()
    context = {
        'articles_list': articles_list
    }

    return render(request, template, context)
