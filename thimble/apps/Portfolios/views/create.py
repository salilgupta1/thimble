from django.shortcuts import render
from django.utils.text import slugify
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

# cloudinary
from cloudinary.forms import cl_init_js_callbacks
from cloudinary.uploader import rename

# models
from thimble.apps.Portfolios.models.schemas.Entry import Entry
from thimble.apps.Portfolios.models.schemas.DesignStory import DesignStory
from thimble.apps.Portfolios.models.schemas.Like import Like
from thimble.apps.Users.models.schemas.Designer import Designer
from thimble.apps.Users.models.schemas.Follow import Follow

# forms 
from thimble.apps.Portfolios.forms.create_forms import *

# ######## WORK HERE
@login_required
def create_design_story(request, username):
    if request.user.username == username:
        context = {}
        if request.method == "POST":
            # form is posted
            design_story_form = CreateDesignStory(request.POST)
            entry_form = CreateEntry(request.POST)

            if design_story_form.is_valid() and entry_form.is_valid():

                # create an instance of the of design_story_model model
                new_design_story = design_story_form.save(commit=False)
                new_design_story.designer = request.user.designer
                new_design_story.save()
                slug = slugify(new_design_story.title)

                # create an instance of the entry model
                new_entry = entry_form.save(commit=False)
                new_entry.design_story = new_design_story
                new_entry.save()

                # update the bucket link
                bucket_link = "%s/%s/%s" % (username, new_design_story.design_story_id, new_entry.entry_id)
                new_entry.bucket_link = bucket_link
                new_entry.save()

                # rename photos pushed to cloudinary
                photos = request.POST.getlist('entry_photos')
                i = 0
                for photo in photos:
                    p = photo.split("/")[3]
                    p = p.split('#')[0].split('.')[0]
                    rename(p, "%s/%s" % (bucket_link, i))
                    i += 1

                return HttpResponseRedirect(
                    reverse('Portfolios:render_design_story', args=(username, new_design_story.design_story_id, slug)))
            else:
                context['error'] = dict(design_story_form.errors.items() + entry_form.errors.items())
        else:

            # page is being "getted"
            context['entry_form'] = CreateEntry(label_suffix='')
            context['design_story_form'] = CreateDesignStory(label_suffix='')
            cl_init_js_callbacks(context['entry_form'], request)
        return render(request, "Portfolios/create_design_story.html", context)

    else:
        raise Http404

# work required....
@login_required
def create_chapter(request, username, story_id, slug):
    context = {}
    if request.user.username == username:
        if request.method == "POST":
            entry_form = CreateEntry(request.POST)
            if entry_form.is_valid():
                new_entry = entry_form.save(commit=False)
                new_entry.design_story_id = story_id
                new_entry.save()

                # update the bucket link
                bucket_link = "%s/%s/%s" % (username, story_id, new_entry.entry_id)
                new_entry.bucket_link = bucket_link
                new_entry.save()

                # rename entry_photos pushed to cloudinary
                photos = request.POST.getlist('entry_photos')
                i = 0
                for photo in photos:
                    p = photo.split("/")[3]
                    p = p.split('#')[0].split('.')[0]
                    rename(p, "%s/%s" % (bucket_link, i))
                    i += 1

                return HttpResponseRedirect(reverse('Portfolios:render_design_story', args=(username, story_id, slug)))
            else:
                context['error'] = entry_form.errors.items()
        else:
            context['entry_form'] = CreateEntry(label_suffix='')
            context['design_story_id'] = story_id
            context['slug'] = slug
            cl_init_js_callbacks(context['entry_form'], request)
        return render(request, "Portfolios/create_chapter.html", context)
    else:
        raise Http404

@login_required
def edit_design_story(request, username):
    pass
