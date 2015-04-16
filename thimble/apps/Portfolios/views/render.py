from django.shortcuts import render
from django.http import Http404
from django.core.context_processors import csrf

# models
from thimble.apps.Portfolios.models.schemas.Entry import Entry
from thimble.apps.Portfolios.models.schemas.DesignStory import DesignStory
from thimble.apps.Portfolios.models.schemas.Like import Like
from thimble.apps.Users.models.schemas.Designer import Designer
from thimble.apps.Users.models.schemas.Follow import Follow

from cloudinary.api import resources


# username refers to portfolio 
def render_portfolio(request, username):
    column_list = ['user', 'user__first_name', 'user__last_name', 'bio', 'avatar', 'following', 'followers']
    portfolio_data = Designer.objects.get_portfolio_data(username=username, column_list=column_list)

    # if portfolio isn't real then raise error
    if portfolio_data is None:
        raise Http404

    context = {"portfolio_data": portfolio_data, "num_pieces": 0}

    # get design_stories related to portfolio
    design_stories = DesignStory.objects.get_design_stories(username=username)

    story_ids = []
    cover_photos = []

    # get cover photos
    if design_stories is not None:
        for story in design_stories:
            story_ids.append(story['design_story_id'])
            cover_photo = Entry.objects.get_cover_photos(story['design_story_id'])
            cover_photos.append(cover_photo)

        context['stories'] = zip(design_stories, cover_photos)
        context['num_pieces'] = len(design_stories)

    # get likes and follow
    if request.user.is_authenticated():
        context['is_following'] = Follow.objects.get_is_following(follower=request.user, followee=portfolio_data['user'])

        if design_stories is not None:
            likes = Like.objects.get_likes(liker=request.user, story_ids=story_ids)
            context['likes'] = likes

    return render(request, "Portfolios/portfolio.html", context)


def render_design_story(request, username, story_id, slug):
    # get portfolio data
    column_list = ['user__first_name', 'user__last_name', 'avatar']
    portfolio_data = Designer.objects.get_portfolio_data(username=username, column_list=column_list)

    # get details of the specific design story
    design_story = DesignStory.objects.get_design_story(username=username, design_story_id=story_id)

    if design_story is None:
        raise Http404

    context = {
        "design_story": design_story,
        "username": username,
        "design_story_id": story_id,
        "portfolio_data": portfolio_data,
        "slug": slug
    }

    # get entries associated with story
    entries = Entry.objects.get_entries(story_id=story_id)

    if entries is not None:
        context['entries'] = entries

        ### get entry photos public_ids from cloudinary
        for entry in entries:
            folder = resources(type="upload", resource_type="image", prefix=entry["bucket_link"])
            num_photos = len(folder['resources'])
            
            entry["photos"] = []
            for i in xrange(num_photos):
                if folder['resources'][i]['public_id'] != entry['cover_photo']:
                    entry["photos"].append(folder['resources'][i]['public_id'])


    return render(request, "Portfolios/story.html", context)
