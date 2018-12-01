# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=20,primary_key='true')
	password = models.CharField(max_length=30)
	name = models.TextField()
	age = models.IntegerField()

	def __str__(self):
		return self.name

class Album(models.Model):
	album_id = models.CharField(max_length=10, primary_key='true')
	name = models.TextField()
	artist = models.TextField()
	name = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Song(models.Model):
	song_id = models.CharField(max_length=10, primary_key='true')
	name = models.TextField()
	album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
	lyric = models.TextField()

	def __str__(self):
		return self.name

class Singer(models.Model):
	singer_id = models.CharField(max_length=10, primary_key='true')
	name = models.TextField()
	description = models.TextField()

	def __str__(self):
		return self.name

class Comment(models.Model):
	user_id = models.ForeignKey(User, on_delete=models.CASCADE)
	singer_id = models.ForeignKey(Song, on_delete=models.CASCADE)
	time = models.DateTimeField()
	content = models.TextField()

	def __str__(self):
		return "%s %s" % (self.user_id, self.singer_id)
