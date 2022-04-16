from django.shortcuts import render
from django.http import JsonResponse
from .models import Article

def add_article(request):
    if(request.method == 'POST'):
        article_text = request.POST.get('text')
        article = Article.objects.create(text=article_text)
        return JsonResponse({'status': 'ok'})