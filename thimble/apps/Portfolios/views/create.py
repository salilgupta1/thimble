from django.shortcuts import render
from django.utils.text import slugify
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

# cloudinary
from cloudinary.forms import cl_init_js_callbacks
from cloudinary.uploader import rename
from cloudinary.api import resources

# utils
from thimble.utils import photo_rename

# models
from thimble.apps.Portfolios.models.schemas.Entry import Entry
from thimble.apps.Portfolios.models.schemas.DesignStory import DesignStory

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
                design_story = design_story_form.save(commit=False)
                design_story.designer = request.user.designer
                design_story.save()

                # create an instance of the entry model
                entry = entry_form.save(commit=False)
                entry.design_story = design_story
                entry.save()

                # update the bucket link
                bucket_link = "%s/%s/%s" % (username, design_story.design_story_id, entry.entry_id)
                entry.bucket_link = bucket_link

                # rename cover_photo
                cover_photo = request.POST.get("cover_photo")
                old_name = photo_rename(bucket_link, [cover_photo])

                entry.cover_photo = "%s/%s" % (bucket_link, old_name)
                entry.save()

                # rename entry_photos pushed to cloudinary
                photos = request.POST.getlist('entry_photos')
                photo_rename(bucket_link, photos)

                slug = slugify(design_story.title)
                return HttpResponseRedirect(
                    reverse('Portfolios:render_design_story', args=(username, design_story.design_story_id, slug)))
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
                # create an instance of the entry model
                entry = entry_form.save(commit=False)
                entry.design_story_id = story_id
                entry.save()

                # update the bucket link
                bucket_link = "%s/%s/%s" % (username, story_id, entry.entry_id)
                entry.bucket_link = bucket_link

                # rename cover_photo
                cover_photo = request.POST.get("cover_photo")
                old_name = photo_rename(bucket_link, [cover_photo])

                entry.cover_photo = "%s/%s" % (bucket_link, old_name)
                entry.save()

                # rename entry_photos pushed to cloudinary
                photos = request.POST.getlist('entry_photos')
                photo_rename(bucket_link, photos)

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
def edit_chapter(request, username, story_id, entry_id, slug):

    context = {
        "username": username,
        "story_id": story_id,
        "entry_id": entry_id,
        "slug": slug
    }

    # get entries associated with story
    print "story_id is {story_id}"
    print "entry_id is {entry_id}"
    entry = Entry.objects.get_entry(story_id=story_id, entry_id=entry_id)
    print entry

    if entry is not None:
        context['entry'] = entry

        ### get entry photos public_ids from cloudinary
        folder = resources(type="upload", resource_type="image", prefix=entry["bucket_link"])
        num_photos = len(folder['resources'])

        entry["photos"] = []
        for i in xrange(num_photos):
            if folder['resources'][i]['public_id'] != entry['cover_photo']:
                entry["photos"].append(folder['resources'][i]['public_id'])

    #
    # if request.method == "POST":
    #     print "post"
    #     edit_entry = EditEntryForm(request.POST, instance=request.user)
    #     if edit_entry.is_valid():
    #         # create an instance of the entry model
    #         entry = edit_entry.save()
    #
    #         # get bucket link from current user
    #
    #         # replace cover_photo field
    #         cover_photo = request.POST.get("cover_photo")
    #         old_name = photo_rename(entry.bucket_link, [cover_photo])
    #         entry.cover_photo = "%s/%s" % (entry.bucket_link, old_name)
    #         entry.save()
    #
    #         # rename entry_photos, new and old
    #         photos = request.POST.getlist('entry_photos')
    #         photo_rename(entry.bucket_link, photos)
    #     else:
    #         context['error'] = edit_entry.errors.items()
    #

    #cl_init_js_callbacks(context['edit_entry'], request)
    # else:
    #     print "not post"


    return render(request, "Portfolios/edit_chapter.html", context)


@login_required
def edit_design_story(request, username):
    pass
