from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

from thimble.apps.Portfolios.models.schemas.Like import Like
from thimble.apps.Users.models.schemas.Follow import Follow
from thimble.apps.Portfolios.models.schemas.Comment import Comment

@login_required
def like_collection(request, username):
    if request.is_ajax():
        liker = request.POST['liker']
        collection_id = request.POST['collection_id']
        try:
            Like.objects.create(liker_id=liker, collection_id=collection_id)
        except:
            raise
    return HttpResponse(True)

@login_required
def unlike_collection(request, username):
    if request.is_ajax():
        liker = request.POST['liker']
        collection_id = request.POST['collection_id']
        try:
            Like.objects.filter(liker_id=liker, collection_id=collection_id).delete()
        except:
            raise
    return HttpResponse(True)

@login_required
def follow_designer(request, username):
    if request.is_ajax():
        follower = request.POST['follower']
        followee = request.POST['followee']
        try:
            Follow.objects.create(follower_id=follower, followee_id=followee)
        except:
            raise
    return HttpResponse(True)

@login_required
def unfollow_designer(request, username):
    if request.is_ajax():
        follower = request.POST['follower']
        followee = request.POST['followee']
        try:
            Follow.objects.filter(follower=follower, followee=followee).delete()
        except:
            raise
    return HttpResponse(True)

@login_required
def comment(request, username):
    if request.is_ajax():
        commenter = request.POST['commenter']
        collection_id = request.POST['collection_id']
        comment = request.POST['comment']
        try:
            Comment.objects.create(commenter_id=commenter, collection_id=collection_id, comment=comment)
        except:
            raise
    return HttpResponse(True)