from django.shortcuts import render
from django.core.context_processors import csrf
import os, chimpy

from thimble.apps.Portfolios.models.schemas.DesignStory import DesignStory
from thimble.apps.Portfolios.models.schemas.Entry import Entry
from thimble.apps.Portfolios.models.schemas.Like import Like

def home(request):
	context = {}
	design_stories = DesignStory.objects.get_all_design_stories()

	story_ids = []

	# get cover photos
	if design_stories is not None:
		cover_photos = []
		for story in design_stories:
			story_ids.append(story['design_story_id'])
			cover_photo = Entry.objects.get_cover_photos(story['design_story_id'])
			cover_photos.append(cover_photo)

	context['stories'] = zip(design_stories, cover_photos)

	# get likes and follow
	if request.user.is_authenticated():
		if design_stories is not None:
			likes = Like.objects.get_likes(liker=request.user, story_ids=story_ids)
			context['likes'] = likes

	return render(request, "landingpage/index.html", context)

def landingpage(request):
	context = {}
	if request.method=="POST":
		email = request.POST.get('email')
		chimp = chimpy.Connection(os.environ['MAILCHIMP_API_KEY'])

		try:
			chimp.list_subscribe(os.environ['MAILCHIMP_LIST_ID'], email, {'FIRST': 'unit', 'LAST': 'tests'}, double_optin=False, send_welcome=True)
		except:
			context['error'] = "We're sorry, it seems there was an error. This may be because you are already signed up."
		else:
			context['success'] = "Thank you for your interest in Thimble!"

	return render(request, "landingpage/new-index.html",context)

def oldlandingpage(request):
	context = {}
	if request.method=="POST":
		email = request.POST.get('email')
		chimp = chimpy.Connection(os.environ['MAILCHIMP_API_KEY'])

		try:
			chimp.list_subscribe(os.environ['MAILCHIMP_LIST_ID'], email, {'FIRST': 'unit', 'LAST': 'tests'}, double_optin=False, send_welcome=True)
		except:
			context['error'] = "We're sorry, it seems there was an error. This may be because you are already signed up."
		else:
			context['success'] = "Thank you for your interest in Thimble!"

	return render(request, "landingpage/old-index.html",context)

