from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import os
from eyed3 import id3

# Create your views here.
def index(request):
	path = "/home/habilis/django-apps/musiconline/staticfiles/music"
	songs = os.listdir(path)
	tag = id3.Tag()
	titles = list()
	artists = list()
	for song in songs:
		tag.parse("staticfiles/music/" + song)
		titles.append(tag.title)
		artists.append(tag.artist)
	songs = zip(titles,artists)
	print(songs)
	template = loader.get_template('playmusic/index.html')
	return HttpResponse(template.render({'songs':list(songs)[:5]},request))

def listenmusic(request):
	template = loader.get_template('playmusic/play.html')
	return HttpResponse(template.render({},request))
