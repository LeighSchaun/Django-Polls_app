
from django.urls import path, include
from . import views
from django.urls import re_path

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    re_path(r'^polls/(?P<question_id>[0-9]+)/$', views.detail, name='detail')
]


