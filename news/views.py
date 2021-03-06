import datetime as dt
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Article

def news_today(request):
    date = dt.date.today()
    news = Article.today_news()
    title = 'News Today'
    return render(request, 'all-news/news.html', {'news': news, 'date': date}, title=title)

def news_of_day(request):
    date = dt.date.today()
    return render(request, 'all-news/today-news.html', {"date": date})

def past_days_news(request, past_date):
    try:
    #converts data from the string url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        #raise 404 error
        raise Http404()
        assert False
    if date == dt.date.today():
        return redirect(news_today)
    news = Article.days_news(date)
    return render(request, 'all-news/past-news.html', {"date": date, "news": news})

def search_results(request):
    if 'article' in request.GET and request.GET['article']:
        search_term = request.GET.get('article')
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'all-news/search.html',{"message": message, "articles": searched_articles})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html', {"message":message})