# #from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
#     #return HttpResponse("Hello Universe! I am home.")
    return render(request, 'home.html')

def about(request):
#        # return HttpResponse("My About page.")
    return render(request, 'about.html')