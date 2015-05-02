from django.contrib import admin
from models.schemas import Comment, DesignStory, Entry, Like

# Register your models here.

admin.site.register(Comment.Comment)
admin.site.register(DesignStory.DesignStory)
admin.site.register(Entry.Entry)
admin.site.register(Like.Like)
