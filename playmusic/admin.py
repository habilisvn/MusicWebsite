from django.contrib import admin

from .models import User, Album, Song, Singer, Comment
# register your models here.
admin.site.register(User)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Singer)
admin.site.register(Comment)
