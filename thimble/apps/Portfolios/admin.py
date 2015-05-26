from django.contrib import admin
from models.schemas import Comment, Collection, Piece, Like

# Register your models here.

admin.site.register(Comment.Comment)
admin.site.register(Collection.Collection)
admin.site.register(Piece.Piece)
admin.site.register(Like.Like)
