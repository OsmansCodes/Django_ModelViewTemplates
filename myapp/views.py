from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def say_hello(request):
    return HttpResponse ("Hello! Django.")

def homepage(request):
    page={
        "title": "Home page",
        "content": "Welcome to our home page"
    }
    return render(request, "index.html", context=page )
def about(request):
    return render(request, "about.html")
def contact(request):
    email="osman@gmail.com"
    social_profiles=[
        "Facebook: fb.com/example",
        "Twitter: twitter.com/example",
        "Github: github.com/example",
        "Instagram: instagram.com/example",
        "YouTube: youtube.com/channelid"
    ]
    hq="b"
    marks="30"
    return render(request, "contact.html",{"emailadd":email, "socialProfiles":social_profiles, "hq":hq, "mark":marks})
def order(request):
    return render(request, "order.html")

def experiment(request, person=None):
    if person is None:
        person="Guest"
    return render(request, "experiment.html", {"data":person})