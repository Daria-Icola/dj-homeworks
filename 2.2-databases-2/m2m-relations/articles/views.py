from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'

    news = Article.objects.all().order_by('-published_at')
    context = {'object_list': news}

    return render(request, template, context)
