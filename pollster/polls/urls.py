from django.urls import path

from . import views

#you can add namespace

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'), #creating a route to view polls/index.html
    path('<int:question_id>/', views.detail, name='detail'), 
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]