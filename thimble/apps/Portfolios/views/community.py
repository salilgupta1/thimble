from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

from thimble.apps.Portfolios.models.schemas.Like import Like
from thimble.apps.Users.models.schemas.Follow import Follow

@login_required
def like_design_story(request, username):
    if request.is_ajax():
        liker = request.POST['liker']
        design_story_id = request.POST['design_story_id']
        try:
            Like.objects.create(liker_id=liker, design_story_id=design_story_id)
        except:
            raise
    return HttpResponse(True)

@login_required
def unlike_design_story(request, username):
    if request.is_ajax():
        liker = request.POST['liker']
        design_story_id = request.POST['design_story_id']
        try:
            Like.objects.filter(liker_id=liker, design_story_id=design_story_id).delete()
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
    pass