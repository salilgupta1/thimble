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

    if collections is not None:

        context['num_pieces'] = len(collections)
        collection_ids = []

        for collection in collections:
            collection_ids.append(collection['id'])
            
            # get collection previews
            bucket_link = "%s/%d" %(username, collection['id'])
            collection["photos"] = []
            try:
                folder = resources(type="upload", resource_type="image", prefix=bucket_link)
                num_photos = len(folder['resources']) 
                num_display = 4 if num_photos > 4 else num_photos
                for i in xrange(0, num_display):
                    collection["photos"].append(folder['resources'][i]['public_id'])
            except:
                pass
        context['collections'] = collections

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
    return render(request, "Portfolios/portfolio.html", context)

def render_collection(request, username, collection_id, slug):
   
    designer = Designer.objects.get_designer_info(username=username)

    # get details of the specific design story
    collection = Collection.objects.get_collection(collection_id=collection_id)
    
    if collection is None:
        raise Http404

    # get comments
    #comments = Comment.objects.get_comments(collection_id=collection_id)

    # get pieces associated with story
    pieces = Piece.objects.get_pieces(collection_id=collection_id)

    context = {
        "collection": collection,
        "pieces":pieces,
        "collection_id": collection_id,
        "username": username,
        "designer": designer,
        "slug": slug,
    }

    return render(request, "Portfolios/collection.html", context)
    