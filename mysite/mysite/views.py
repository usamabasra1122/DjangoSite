from ast import Return
import turtle
from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import redirect, render


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


def user_form(request):

    try:
            
            name= request.POST["fname"]
            num= request.POST["fnum"]
            num1= request.POST["num"]
        

            print("user name is " + str(name) + " number is  :" + str(num))

            url= "/aboutus/?output={}".format(name)

            if request.POST.get("num") == "":
               return render(request, "userform.html" , {'error':True})
               
            return HttpResponseRedirect(url)  




            
    except:
        pass

    return render(request, "userform.html" )