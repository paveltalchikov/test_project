from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    now = datetime.now()

    return render(
        request,
        "MyApp1/index.html",
            {
                'title' : "Hi Jango",
                'message' : "hello Jango",
                'content': " performed on " + now.strftime("%A, %d %B, %Y at %X")
            }
        )