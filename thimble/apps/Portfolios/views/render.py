from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

# models
from thimble.apps.Portfolios.models.schemas.Piece import Piece
from thimble.apps.Portfolios.models.schemas.Collection import Collection
from thimble.apps.Portfolios.models.schemas.Like import Like

from thimble.apps.Users.models.schemas.Designer import Designer
from thimble.apps.Users.models.schemas.Buyer import Buyer
from thimble.apps.Users.models.schemas.Follow import Follow
from django.contrib.contenttypes.models import ContentType

from taggit.models import TaggedItem

from cloudinary.api import resources

@login_required
def render_portfolio(request, username):
    designer = Designer.objects.get_designer_info(username=username)

    # if portfolio isn't real then raise error
    if designer is None:
        raise Http404

    context = {"designer": designer, "num_collections": 0}
    context['favorites'] = Like.objects.get_favorite_count(liker=designer)
    
    # get collections related to portfolio
    collections = Collection.objects.get_collections(username=username)
    if collections is not None:

        context['num_collections'] = len(collections)
        for collection in collections:
            collection['tags'] = Collection.objects.get_tags(collection_id=collection['id'])
            
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

        # get if liked by user for each collection
        try:
            liker = request.user.buyer
        except AttributeError:
            liker = request.user.designer

        likes = Like.objects.get_likes(liker=liker)    
        context['likes'] = likes

    # get follow 
    if request.user.username != username:
        try:
            follower = request.user.buyer
        except AttributeError:
            follower = request.user.designer

        context['is_following'] = Follow.objects.get_is_following(follower=follower, followee=designer) 
    return render(request, "Portfolios/portfolio.html", context)

@login_required
def render_collection(request, username, collection_id, slug):
   
    designer = Designer.objects.get_designer_info(username=username)

    # get details of the specific design story
    collection = Collection.objects.get_collection(collection_id=collection_id)
    if collection is None:
        raise Http404
    tags = Collection.objects.get_tags(collection_id=collection_id)
    
    try:
        liker = request.user.buyer
    except:
        liker = request.user.designer

    is_liked = Like.objects.get_is_liked(liker=liker, collection_id=collection_id)
    
    # get pieces associated with story
    pieces = Piece.objects.get_pieces(collection_id=collection_id, column_list=["piece_title","front_view"])

    context = {
        "collection": collection,
        "pieces":pieces,
        "collection_id": collection_id,
        "designer": designer,
        "slug": slug,
        "tags":tags,
        "is_liked":is_liked
    }

    return render(request, "Portfolios/collection.html", context)

@login_required
def render_linesheet(request, username, collection_id, slug):
    pieces = Piece.objects.get_pieces(collection_id=collection_id, column_list = ["piece_title", "front_view", "details", "wholesale_price","retail_price","min_quantity","product_number"])
    context = {"pieces":pieces}
    return render(request, "Portfolios/linesheet.html", context)

@login_required
def search(request, username):
    context = {}
    context["buyer_tags"] = TaggedItem.objects.filter(content_type_id=ContentType.objects.get_for_model(Buyer())).values("tag_id__name").distinct()
    context["buyers"] = Buyer.objects.all().values('boutique_name','location','bio','avatar','user__first_name','user__last_name')
    return render(request, "Portfolios/search.html", context)

def filter_tags(request, username):
    if request.method == 'POST' and request.is_ajax():
        selected_tags = request.POST.getlist('tag-filters[]')

        if len(selected_tags) == 0:
            buyers = Buyer.objects.all().values('boutique_name','location','bio','avatar','user__first_name','user__last_name')
        else:
            buyers = Buyer.objects.filter(tags__name__in=selected_tags).distinct().values('boutique_name','location','bio','avatar','user__first_name','user__last_name')

        response = {'buyers':list(buyers)}

        return JsonResponse(response)

