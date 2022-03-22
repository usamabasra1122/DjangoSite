
from django.http import HttpResponse
from django.shortcuts import render


def aboutUs(request):
    return HttpResponse("<h1>Wellcome the MyPage</h1>")

def homepage(request):
    return render(request, "index.html")
