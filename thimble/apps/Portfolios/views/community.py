from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

# models
from thimble.apps.Portfolios.models.schemas.Like import Like
from thimble.apps.Users.models.schemas.Follow import Follow
from thimble.apps.Portfolios.models.schemas.Comment import Comment
from thimble.apps.Users.models.schemas.Designer import Designer
from thimble.apps.Users.models.schemas.Buyer import Buyer

@login_required
def liking(request, username):
    if request.is_ajax():
        try:
            liker = request.user.buyer
        except AttributeError:
            liker = request.user.designer

        collection_id = request.POST['collection_id']
        is_liking = int(request.POST['is_liking'])

        try:
            if is_liking:
                # like
                Like.objects.create(object_id=liker.pk, content_type=liker.get_ct(), collection_id=collection_id)
            else:
                # unlike
                Like.objects.filter(object_id=liker.pk, content_type=liker.get_ct(), collection_id=collection_id).delete()
        except:
            raise

    return HttpResponse(True)

@login_required
def following(request, username):
    if request.is_ajax():
        try:
            follower = request.user.designer
        except AttributeError:
            follower = request.user.buyer

        try:
            followee = Designer.objects.get(user_id=username)
        except:
            followee = Buyer.objects.get(user_id=username)

        is_following = int(request.POST['is_following'])
        
        try:
            if is_following:
                # follow
                Follow.objects.create(
                    follower_object_id=follower.pk, 
                    follower_content_type=follower.get_ct(), 
                    followee_object_id=followee.pk, 
                    followee_content_type=followee.get_ct())
            else:
                # unfollow
                Follow.objects.filter(
                    follower_object_id=follower.pk, 
                    follower_content_type=follower.get_ct(), 
                    followee_object_id=followee.pk, 
                    followee_content_type=followee.get_ct()).delete()
        except:
            raise
    return HttpResponse(True)

@login_required
def comment(request, username):
    if request.is_ajax():
        try:
            commenter = request.user.designer
        except AttributeError:
            commenter = request.user.buyer

        collection_id = request.POST['collection_id']
        comment = request.POST['comment']

        try:
            Comment.objects.create(content_type=commenter.get_ct(), object_id = commenter.pk, collection_id=collection_id, comment=comment)
        except:
            raise
    return HttpResponse(True)

    