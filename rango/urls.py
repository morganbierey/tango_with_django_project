from django.urls import path
from rango import views
app_name = 'rango'
urlpatterns = [
path('', views.index, name='index'),
]

#this is the urls.py file which is mentioned  (to create) in section 3.5 of twd 