from django.shortcuts import render

from django.http import HttpResponse
def index(request):
    return HttpResponse("Rango says hey there partner!<a href='/rango/about/'>About</a>")#edited in excercise 3.6<>
    
    

#below is the new method from excercise 3.6
def about(request):
    return HttpResponse("Rango says here is the about page.<a href='/rango/'>Index</a>.")#edited in excercise 3.6 <>