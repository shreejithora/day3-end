from django.shortcuts import render
from django.http import HttpResponse
import datetime
import time
import requests
import bs4


def home(request):
    page = requests.get('https://fabpedigree.com/james/mathmen.htm')
    soup = bs4.BeautifulSoup(page.content,'html.parser')
    li = [tag.string for tag in soup.select('ol a')]
    d = {
        'names':li,
        'hundred_mathematicians': len(li)
        }
    return render(request, 'index.html', d)
    # return HttpRes
    # ponse('Greetings. Welcome to the time machine.')


def today(request):
    date = datetime.date.today()
    return HttpResponse("Today's date is: {}".format(date))


def timestamp(request):
    ts = time.time()
    return HttpResponse("Timestamp: {}".format(ts))
