from django.shortcuts import render
from django.core.context_processors import csrf
import os, chimpy
from thimble.apps.Portfolios.models.schemas.Like import Like
from thimble.apps.Portfolios.models.schemas.Collection import Collection
from taggit.models import Tag

import json
from django.http import HttpResponse


def home(request):
    # new-home-page
    context = {}
    all_tags = Tag.objects.all()
    context["all_tags"] = all_tags

    if request.method == 'POST' and request.is_ajax():
        selected_tags = request.POST.getlist('tag-filters[]')
        if len(selected_tags) == 0:
            collections = Collection.objects.all()
        else:
            collections = Collection.objects.filter(tags__name__in=selected_tags).distinct()

        response = {'collections': list(collections.values('title'))}
        return HttpResponse(json.dumps(response))

    collections = Collection.objects.all()
    context["collections"] = collections
    return render(request, "landingpage/index.html", context)


def landingpage(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get('email')
        chimp = chimpy.Connection(os.environ['MAILCHIMP_API_KEY'])

        try:
            chimp.list_subscribe(os.environ['MAILCHIMP_LIST_ID'], email, {},
                                 double_optin=False, send_welcome=True)
        except:
            context[
                'error'] = "We're sorry, it seems there was an error. This may be because you haves already signed up."
        else:
            context['success'] = "Thank you for your interest in Thimble!"

    return render(request, "landingpage/beta.html", context)

# about/
def oldlandingpage(request):
    context = {}
    return render(request, "landingpage/about.html", context)

