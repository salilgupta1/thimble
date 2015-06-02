from django.shortcuts import render
from django.core.context_processors import csrf
import os, chimpy

from thimble.apps.Portfolios.models.schemas.Collection import Collection
from taggit.models import Tag
from django.template.defaultfilters import slugify
import json
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse


def home(request):
    try:
        if request.user.buyer is not None:
            return HttpResponseRedirect(reverse('landingpage:dashboard', args=(request.user.username,)))
    except:
        return HttpResponseRedirect(reverse('Portfolios:render_portfolio', args=(request.user.username,)))

@login_required
def dashboard(request, username):
    if request.user.username == username:
        context = {}
        all_tags = Tag.objects.all()
        context["all_tags"] = all_tags

        if request.method == 'POST' and request.is_ajax():
            selected_tags = request.POST.getlist('tag-filters[]')
            if len(selected_tags) == 0:
                collections = Collection.objects.all()
            else:
                collections = Collection.objects.filter(tags__name__in=selected_tags).distinct()

            # I couldn't figure out how to construct the URL cleanly and give it to the ajax response
            collection_add_info = {}
            for collection in collections:
                collection_add_info[collection.title] = reverse("Portfolios:render_collection", args=(collection.designer.user.username, collection.id, slugify(collection.title)))
            
            response = {'collections': list(collections.values('designer','title')), 'add_info':collection_add_info}
            return HttpResponse(json.dumps(response))

        collections = Collection.objects.all()
        context["collections"] = collections
        return render(request, "landingpage/dashboard.html", context)
    else:
        raise Http404

def landingpage(request):
    context = {}
    if request.method == "POST":
        email = request.POST.get('email')
        chimp = chimpy.Connection(os.environ['MAILCHIMP_API_KEY'])

        try:
            chimp.list_subscribe(os.environ['MAILCHIMP_LIST_ID'], email, {},
                                 double_optin=False, send_welcome=True)
        except:
            context['error'] = "We're sorry, it seems there was an error. This may be because you have already signed up."
        else:
            context['success'] = "Thank you for your interest in Thimble!"

    return render(request, "landingpage/beta.html", context)

# about/
def oldlandingpage(request):
    context = {}
    return render(request, "landingpage/about.html", context)

