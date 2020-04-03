from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), #creating a route to view polls/index.html
    
]