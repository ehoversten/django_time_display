from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from datetime import date, datetime

# Create your views here.
def index(request):
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

    data = {

        "time_now": strftime("%Y-%m-%d %H:%M %p", gmtime())

        # "time_now" : datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
    }

    return render(request, 'time_display/index.html', data)
