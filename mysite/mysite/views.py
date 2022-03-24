from django.http import HttpResponse
from django.shortcuts import render


def aboutUs(request):
    return HttpResponse("<h1>Wellcome the MyPage</h1>")

def homepage(request):
    data ={
        'page_header':'This is Table View',
        'student': [ 
            {'id': 1 , 'name':'usama'},
            {'id':2,  'name': 'Ali'}


        ]


    }
    return render(request, "index.html", data)
