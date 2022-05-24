import datetime as dt
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Article
# Create your views here.
# def welcome(request):
#     return render(request, 'welcome.html')

def news_today(request):
    date = dt.date.today()
    news = Article.today_news()
    return render(request, 'all-news/news.html', {'news': news, 'date': date})

def news_of_day(request):
    date = dt.date.today()
    
    # Function to convert date object to find exact day
    # day = convert_dates(date)
    # html = f'''
    # <html>
    #     <body>
    #         <h1>News for {day} </h1> <em> {date.day}-{date.month}-{date.year} </em>
    #     </body>
    # </html>
    # '''
    # return HttpResponse(html)
    return render(request, 'all-news/today-news.html', {"date": date})

# def convert_dates(dates):
#     #function that gets the weekday number for the date 
#     day_number = dt.date.weekday(dates)
    
#     days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
#     #returning the actualday of the week
#     day = days[day_number]
#     return day

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
    # day = convert_dates(date)
    # html = f'''
    # <html>
    # <body>News for {day} {date.day}-{date.month}-{date.year}</body>
    # </html>
    # '''
    # return HttpResponse(html)