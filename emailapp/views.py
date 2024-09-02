from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def getmail(request):
    return render(request, "email.html")