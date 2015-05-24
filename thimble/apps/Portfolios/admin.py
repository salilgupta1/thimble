from django.contrib import admin
from models.schemas import Comment, Collection, Entry, Like

# Register your models here.

admin.site.register(Comment.Comment)
admin.site.register(Collection.Collection)
admin.site.register(Entry.Entry)
admin.site.register(Like.Like)
