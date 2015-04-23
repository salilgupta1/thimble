from django.shortcuts import render
from django.utils.text import slugify
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

# cloudinary
from cloudinary.forms import cl_init_js_callbacks
from cloudinary.uploader import rename
from cloudinary.api import resources, delete_resources

# utils
from thimble.utils import photo_rename

# models
from thimble.apps.Portfolios.models.schemas.Entry import Entry
from thimble.apps.Portfolios.models.schemas.DesignStory import DesignStory

# forms 
from thimble.apps.Portfolios.forms.forms import *

@login_required
def create_design_story(request, username):

    if request.user.username == username:
        design_story_form = CreateDesignStory(request.POST or None)
        entry_form = CreateEntry(request.POST or None)

        if request.method == "POST":
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

                # rename entry_photos 
                photos = request.POST.getlist('entry_photos')
                photo_rename(bucket_link, photos)

                slug = slugify(design_story.title)

                return HttpResponseRedirect(
                    reverse('Portfolios:render_design_story', args=(username, design_story.design_story_id, slug)))

        context = {
            "design_story_form":design_story_form,
            "entry_form":entry_form
        }
        
        cl_init_js_callbacks(context['entry_form'], request)
        return render(request, "Portfolios/create_design_story.html", context)
    else:
        raise Http404

@login_required
def create_chapter(request, username, story_id, slug):

    if request.user.username == username:
        entry_form = CreateEntry(request.POST or None)
        if request.method == "POST":
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

        context = {
            "entry_form":entry_form,
            "design_story_id":story_id,
            "slug":slug
        }

        cl_init_js_callbacks(context['entry_form'], request)
        return render(request, "Portfolios/create_chapter.html", context)
    else:
        raise Http404

@login_required
def edit_chapter(request, username, story_id, slug, entry_id,):

    context = {
        "username": username,
        "story_id": story_id,
        "entry_id": entry_id,
        "slug": slug
    }

    # TODO handle exception when entry does not exist
    # get entry to be edited
    e_instance = Entry.objects.get(entry_id=entry_id)
    entry = {}
    entry['cover_photo'] = e_instance.cover_photo
    entry['entry_title'] = e_instance.entry_title

    if entry is not None:
        context['entry'] = entry

        # get entry photos public_ids from cloudinary
        folder = resources(type="upload", resource_type="image", prefix=e_instance.bucket_link)
        num_photos = len(folder['resources'])

        entry["photos"] = []
        for i in xrange(num_photos):
            if folder['resources'][i]['public_id'] != entry['cover_photo']:
                entry["photos"].append(folder['resources'][i]['public_id'])

    if request.method == "POST":
        edit_entry = EditEntry(request.POST, instance=e_instance)
        if edit_entry.is_valid():

            # replace cover_photo
            # automatically makes the old cover into a supplementary photo
            new_cover = request.POST.get("cover_photo")
            if new_cover is not None:
                old_name = photo_rename(e_instance.bucket_link, [new_cover])
                e_instance.cover_photo = "%s/%s" % (e_instance.bucket_link, old_name)

                # make sure the updated chapter is displayed
                entry["photos"].append(entry["cover_photo"])
                entry['cover_photo'] = e_instance.cover_photo

            e_instance.save()

            # rename new entry_photos
            photos = request.POST.getlist('entry_photos')
            if photos is not None:
                for p in photos:
                    entry["photos"].append("%s/%s" % (e_instance.bucket_link, photo_rename(e_instance.bucket_link, [p])))

            # delete photos marked for deletion
            to_be_deleted = request.POST.getlist('photo_delete')
            if len(to_be_deleted) != 0:
                if len(entry["photos"]) - len(to_be_deleted) <= 0:
                    context['error'] = "Could not delete images; must have at least one remaining"
                else:
                    delete_resources(to_be_deleted)
                    for item in to_be_deleted:
                        entry["photos"].remove(item)

            context['changes_saved'] = "Changes saved."

        else:
            context['error'] = edit_entry.errors.items()
    else:
        edit_entry = EditEntry(instance=e_instance)

    context['edit_entry'] = edit_entry
    context['entry'] = entry
    cl_init_js_callbacks(context['edit_entry'], request)

    return render(request, "Portfolios/edit_chapter.html", context)

@login_required
def edit_story(request, username, story_id, slug):
    context = {
        "username": username,
        "story_id": story_id,
        "slug": slug
    }
    # TODO handle exception when story does not exist
    # get story to be edited
    s_instance = DesignStory.objects.get(design_story_id=story_id)
    story = {}
    story['title'] = s_instance.title
    story['description'] = s_instance.description
    story['wip'] = s_instance.wip

    # get entries associated with story
    entries = Entry.objects.get_entries(story_id=story_id)

    if entries is not None:

        for entry in entries:
            # make api call to get public id's
            folder = resources(type="upload", resource_type="image", prefix=entry["bucket_link"])
            num_photos = len(folder['resources'])

            # pull public id's out of json response
            entry["photos"] = []
            for i in xrange(num_photos):
                if folder['resources'][i]['public_id'] != entry['cover_photo']:
                    entry["photos"].append(folder['resources'][i]['public_id'])

    if request.method == "POST":
        edit_dstory = EditDesignStory(request.POST, instance=s_instance)
        if edit_dstory.is_valid():
            edit_dstory.save()

            # delete chapters marked for deletion
            to_be_deleted = request.POST.getlist('photo_delete')
            if len(to_be_deleted) != 0:
                if len(entries) - len(to_be_deleted) <= 0:
                    context['error'] = "Could not delete entries; must have at least one remaining"
                else:
                    for i, e in enumerate(entries):
                        if str(e['entry_id']) in to_be_deleted:
                            # remove from context
                            entries = entries.exclude(entry_id=e['entry_id'])

                            # delete associated images from cloudinary
                            for p in e['photos']:
                                delete_resources([p])
                                break
                            delete_resources([e['cover_photo']])

                            # delete from db
                            Entry.objects.get(entry_id=e['entry_id']).delete()

            context['changes_saved'] = "Changes saved."
        else:
            context['error'] = edit_dstory.errors.items()
    else:
        edit_dstory = EditDesignStory(instance=s_instance)

    context['entries'] = entries
    context['edit_story'] = edit_dstory
    context['story'] = story
    cl_init_js_callbacks(context['edit_story'], request)

    return render(request, "Portfolios/edit_story.html", context)
