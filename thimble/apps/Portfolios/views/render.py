from django.shortcuts import render
from django.http import Http404
from django.core.context_processors import csrf

# models
from thimble.apps.Portfolios.models.schemas.Entry import Entry
from thimble.apps.Portfolios.models.schemas.DesignStory import DesignStory
from thimble.apps.Portfolios.models.schemas.Like import Like
from thimble.apps.Portfolios.models.schemas.Comment import Comment

from thimble.apps.Users.models.schemas.Designer import Designer
from thimble.apps.Users.models.schemas.Follow import Follow

from cloudinary.api import resources

# username refers to portfolio 
# request.user refers to user that is logged in

def render_portfolio(request, username):
    column_list = ['user', 'user__first_name', 'user__last_name', 'bio', 'avatar', 'following', 'followers']
    portfolio_data = Designer.objects.get_portfolio_data(username=username, column_list=column_list)

    # if portfolio isn't real then raise error
    if portfolio_data is None:
        raise Http404

    context = {"portfolio_data": portfolio_data, "num_pieces": 0}
    context['favorites'] = Like.objects.get_favorites(liker=username)
    
    # get design_stories related to portfolio
    design_stories = DesignStory.objects.get_design_stories(username=username)

    story_ids = []

    # get cover photos
    if design_stories is not None:
        cover_photos = []

        for story in design_stories:
            story_ids.append(story['design_story_id'])

            ## OPTIMIZE (Salil Gupta)
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
    
    # get comments
    comments = Comment.objects.get_comments(design_story_id=story_id)

    if design_story is None:
        raise Http404

    # get entries associated with story
    entries = Entry.objects.get_entries(story_id=story_id)

    if entries is not None:

        ### get entry photos public_ids from cloudinary
        ### OPTIMIZE (Salil Gupta)
        for entry in entries:
            # make api call to get public id's
            folder = resources(type="upload", resource_type="image", prefix=entry["bucket_link"])
            num_photos = len(folder['resources'])
            
            # pull public id's out of json response
            entry["photos"] = []
            for i in xrange(num_photos):
                if folder['resources'][i]['public_id'] != entry['cover_photo']:
                    entry["photos"].append(folder['resources'][i]['public_id'])

    context = {
        "design_story": design_story,
        "story_id": story_id,
        "username": username,
        "portfolio_data": portfolio_data,
        "slug": slug,
        "comments":comments,
        "entries":entries
    }

    return render(request, "Portfolios/story.html", context)