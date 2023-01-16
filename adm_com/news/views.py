from django.shortcuts import render, HttpResponse


def index(request):
    template = 'news/index.html'
    return render(request, template)