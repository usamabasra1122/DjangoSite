from django.http import HttpResponse
from django.shortcuts import render


def aboutus(request):
    return render(request, "about_us.html")

def homepage(request):
    data ={
        'page_header':'This is Table View',
        'student': [ 
            {'id': 1 , 'name':'usama'},
            {'id':2,  'name': 'Ali'}


        ]


    }
    return render(request, "index.html", data)
