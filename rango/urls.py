from django.urls import path
from rango import views
app_name = 'rango'
urlpatterns = [
path('', views.index, name='index'),
path('', views.about, name ='about'), #new line added excercise 3.6
]

#this is the urls.py file which is mentioned  (to create) in section 3.5 of twd 