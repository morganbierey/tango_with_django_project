from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    #edited in excercise 3.6<>
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")
    
    

#below is the new method from excercise 3.6
def about(request):
    #edited in excercise 3.6<>
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")