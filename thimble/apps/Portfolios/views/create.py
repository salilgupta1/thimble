from django.shortcuts import render
from django.utils.text import slugify
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
import json

# cloudinary
from cloudinary.forms import cl_init_js_callbacks
from cloudinary.uploader import rename
from cloudinary.api import resources, delete_resources

# utils
from thimble.utils import photo_rename

# models
from thimble.apps.Users.models.schemas.Designer import Designer
from thimble.apps.Portfolios.models.schemas.Piece import Piece
from thimble.apps.Portfolios.models.schemas.Collection import Collection
from django.db import IntegrityError

# forms 
from thimble.apps.Portfolios.forms.forms import *

@login_required
def create_collection(request, username):
    error = None
    if request.user.username == username:
        collection_form = CreateCollection(request.POST or None)
        if request.method =="POST":
            if collection_form.is_valid():
                collection = collection_form.save(commit=False)
                collection.designer = request.user.designer

                try:
                    collection.save()
                    collection_form.save_m2m()
                except IntegrityError:
                    error = "Sorry! You are already using this title for another collection"

                # photos
                folder_link = "%s/%s" % (username, collection.pk)
                photos = request.POST.getlist("images")
                pieces = photo_rename(folder_link, photos)

                for piece in pieces:
                    Piece.objects.create(collection_id=collection.pk, front_view=piece)

                if not error:
                    slug = slugify(collection.title)
                    return HttpResponseRedirect(reverse('Portfolios:create_linesheet', args=(username, collection.pk, slug)))
            
        context = {
            "collection_form":collection_form,
            "error":error or None
        }

        cl_init_js_callbacks(context['collection_form'], request)
        return render(request, "Portfolios/create_collection.html", context)
    else:
        raise Http404

@login_required
def create_linesheet(request, username, collection_id, slug):
    context = {}
    pieces = Piece.objects.filter(collection_id=collection_id)
    piece_forms = [PieceForm(request.POST or None, prefix=piece.piece_id, instance=piece) for piece in pieces]
    images = [piece.front_view for piece in pieces]

    if request.method == "POST":       
        if all([pf.is_valid() for pf in piece_forms]):
            for pf in piece_forms:
                pf.save()
            return HttpResponseRedirect(reverse('Portfolios:render_collection', args=(username, collection_id, slug)))    
    
    context['pieces'] = zip(piece_forms, images)
    context['username'] = username
    context['collection_id'] = collection_id
    context['slug'] = slug

    return render(request, "Portfolios/create_linesheet.html", context)

    