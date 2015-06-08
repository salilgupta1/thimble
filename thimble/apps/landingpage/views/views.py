from django.shortcuts import render
from django.core.context_processors import csrf
import os, chimpy

from thimble.apps.Portfolios.models.schemas.Collection import Collection
from thimble.apps.Portfolios.models.schemas.Piece import Piece
from thimble.apps.Portfolios.models.schemas.Like import Like

from thimble.apps.Users.models.schemas.Follow import Follow
from thimble.apps.Users.models.schemas.Designer import Designer


from taggit.models import Tag
from django.template.defaultfilters import slugify
import json

from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.core import serializers

def home(request):
    try:
        if request.user.buyer is not None:
            return HttpResponseRedirect(reverse('landingpage:dashboard', args=(request.user.username,)))
    except:
        try:
            if request.user.designer is not None:
                return HttpResponseRedirect(reverse('Portfolios:render_portfolio', args=(request.user.username,)))
        except:
            return HttpResponseRedirect(reverse("Users:login"))

@login_required
def dashboard(request, username):
    if request.user.username == username:
        context = {}
        all_tags = Tag.objects.all()
        context["all_tags"] = all_tags
        context["collections"] = Collection.objects.all().values('designer','title','id','description','designer__avatar','designer__user__first_name','designer__user__last_name')
        context['pieces'] = Piece.objects.all().values('collection_id','front_view')
        print context
        return render(request, "landingpage/dashboard.html", context)
    else:
        raise Http404

def filter_by_tags(request):
    if request.method == 'POST' and request.is_ajax():
        selected_tags = request.POST.getlist('tag-filters[]')
        
        if len(selected_tags) == 0:
            collections = Collection.objects.all().values('designer','title','id','description','designer__avatar','designer__user__first_name','designer__user__last_name')
        else:
            collections = Collection.objects.filter(tags__name__in=selected_tags).distinct().values('designer','title','id','description','designer__avatar','designer__user__first_name','designer__user__last_name')
        
        if collections:
            for collection in collections:
                collection['pieces'] = list(Piece.objects.filter(collection_id=collection['id']).values_list('front_view',flat=True))
                collection['url'] = reverse("Portfolios:render_collection", args=(collection['designer'], collection['id'], slugify(collection['title'])))

            response = {'collections':list(collections)}
        else:
            response = {'collections':[]}
        return JsonResponse(response)

def render_followers_list(request):
    if request.method == "POST" and request.is_ajax():
        following = Follow.objects.get_following(request.user.buyer)
        
        if following:
            response = {'following': list(Designer.objects.filter(id__in=following).values("user_id","bio","location","avatar","user__first_name","user__last_name"))}
        else:
            response = {'following':[]}
        return JsonResponse(response)

def render_favorites_list(request):
    if request.method == "POST" and request.is_ajax():
        favorites = Like.objects.get_likes(request.user.buyer)
        collections = Collection.objects.filter(id__in=favorites).values('designer','title','id','description','designer__avatar','designer__user__first_name','designer__user__last_name')
        
        if collections:
            for collection in collections:
                collection['pieces'] = list(Piece.objects.filter(collection_id=collection['id']).values_list('front_view',flat=True))
                collection['url'] = reverse("Portfolios:render_collection", args=(collection['designer'], collection['id'], slugify(collection['title'])))

            response = {'collections':list(collections)}
        else:
            response = {'collections':[]}
        return JsonResponse(response)

def landingpage(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get('email')
        chimp = chimpy.Connection(os.environ['MAILCHIMP_API_KEY'])

        try:
            chimp.list_subscribe(os.environ['MAILCHIMP_LIST_ID'], email, {}, double_optin=False, send_welcome=True)
        except:
            context['error'] = "We're sorry, it seems there was an error. This may be because you have already signed up."
        else:
            context['success'] = "Thank you for your interest in Thimble!"

    return render(request, "landingpage/beta.html", context)

# about/
def oldlandingpage(request):
    context = {}
    return render(request, "landingpage/about.html", context)

