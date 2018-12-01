from django.conf.urls import url
from django.urls import path

from . import views

app_name = "playmusic"
urlpatterns = [
	path('', views.index, name = 'index'),
	path('play/', views.listenmusic, name = 'play'),
]
