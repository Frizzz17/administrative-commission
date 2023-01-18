from django.contrib import admin
from news.models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('header', 'text', 'date')


admin.site.register(News, NewsAdmin)
