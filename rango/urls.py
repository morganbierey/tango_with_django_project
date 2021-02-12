
from django.urls import path
from rango import views
app_name = 'rango'

##edited 7.2

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category,
    name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
]


#this is the urls.py file which is mentioned  (to create) in section 3.5 of twd 

#added path() in the above in chptr 7 ex