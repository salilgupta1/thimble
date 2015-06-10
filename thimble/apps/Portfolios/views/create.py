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
                    return HttpResponseRedirect(reverse('Portfolios:edit_collection', args=(username, collection.pk, slug)))
            
        context = {
            "collection_form":collection_form,
            "error":error or None
        }

        cl_init_js_callbacks(context['collection_form'], request)
        return render(request, "Portfolios/create_collection.html", context)
    else:
        raise Http404

@login_required
def edit_collection(request, username, collection_id, slug):
    context = {}
    if request.user.username == username:
        if request.is_ajax():
            pieces = json.loads(request.POST['pieces'])
            for piece in pieces:
                p = Piece.objects.get(piece_id=piece['id'])
                p.piece_title = piece["title"]
                p.save(update_fields=["piece_title"])

            response = {"status":1, "redirect_url":reverse("Portfolios:render_collection", args=(username, collection_id, slug))}
            return HttpResponse(json.dumps(response), content_type="application/json")

        else:
            pieces = Piece.objects.get_pieces(collection_id)
           
            context['pieces'] = pieces
            context['username'] = username
            context['collection_id'] = collection_id
            context['slug'] = slug

            return render(request, "Portfolios/edit_collection.html", context)
    else:
        raise Http404
    # a restricted editing option
    # edit title, description, tags of collection
    # edit title of pieces

    


    