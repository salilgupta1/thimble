from django.shortcuts import render
from django.http import Http404
from django.core.context_processors import csrf

# models
from thimble.apps.Portfolios.models.schemas.Piece import Piece
from thimble.apps.Portfolios.models.schemas.Collection import Collection
from thimble.apps.Portfolios.models.schemas.Like import Like
from thimble.apps.Portfolios.models.schemas.Comment import Comment

from thimble.apps.Users.models.schemas.Designer import Designer
from thimble.apps.Users.models.schemas.Follow import Follow

from cloudinary.api import resources

def render_portfolio(request, username):
    designer = Designer.objects.get_designer_info(username=username)

    # if portfolio isn't real then raise error
    if designer is None:
        raise Http404

    context = {"designer": designer, "num_pieces": 0}
    context['favorites'] = Like.objects.get_favorites(liker=designer)
    
    # get collections related to portfolio
    collections = Collection.objects.get_collections(username=username)

    # get collection previews
    if collections is not None:
        collection_ids = []
        for collection in collections:
            collection_ids.append(collection['id'])

        context['num_pieces'] = len(collections)

        # get previews for each collection here

        # get if liked by authenticated user for each collection
        if request.user.is_authenticated():
            try:
                liker = request.user.buyer
            except AttributeError:
                liker = request.user.designer

            likes = Like.objects.get_likes(liker=liker, collection_ids=collection_ids)    
            context['likes'] = likes

    # get follow 
    if request.user.is_authenticated() and request.user.username != username:
        try:
            follower = request.user.buyer
        except AttributeError:
            follower = request.user.designer

        context['is_following'] = Follow.objects.get_is_following(follower=follower, followee=designer)
    context['collections'] = collections
    return render(request, "Portfolios/portfolio.html", context)

def render_collection(request, username, collection_id, slug):
   
    avatar = Designer.objects.get_avatar(username=username)

    # get details of the specific design story
    collection = Collection.objects.get_collection(collection_id=collection_id)
    
    if collection is None:
        raise Http404

    # get comments
    #comments = Comment.objects.get_comments(collection_id=collection_id)

    # get pieces associated with story
    # entries = Entry.objects.get_entries(story_id=story_id)

    # if entries is not None:

    #     ### get entry photos public_ids from cloudinary
    #     ### OPTIMIZE (Salil Gupta)
    #     for entry in entries:
    #         # make api call to get public id's
    #         folder = resources(type="upload", resource_type="image", prefix=entry["bucket_link"])
    #         num_photos = len(folder['resources'])
            
    #         # pull public id's out of json response
    #         entry["photos"] = []
    #         for i in xrange(num_photos):
    #             if folder['resources'][i]['public_id'] != entry['cover_photo']:
    #                 entry["photos"].append(folder['resources'][i]['public_id'])

    context = {
        "collection": collection,
        "collection_id": collection_id,
        "username": username,
        "avatar": avatar,
        "slug": slug,
        #"comments":comments,
    }

    return render(request, "Portfolios/collection.html", context)
    