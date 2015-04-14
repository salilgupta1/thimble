from django.shortcuts import render
from django.utils.text import slugify
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

# cloudinary
from cloudinary.forms import cl_init_js_callbacks
from cloudinary.uploader import rename

# models
from thimble.apps.Portfolios.models.schemas.Entry import Entry
from thimble.apps.Portfolios.models.schemas.DesignStory import DesignStory
from thimble.apps.Users.models.schemas.Designer import Designer
from thimble.apps.Portfolios.models.schemas.Like import Like
from thimble.apps.Users.models.schemas.Follow import Follow

# forms 
from thimble.apps.Portfolios.forms.create_forms import *

# username refers to portfolio 
def render_portfolio(request, username):
	column_list = ['user','user__first_name','user__last_name','bio','avatar','following','followers']
	portfolio_data = Designer.objects.get_portfolio_data(username = username, column_list = column_list)

	# if portfolio isn't real then raise error
	if portfolio_data == None:
		raise Http404

	context = {"portfolio_data":portfolio_data, "num_pieces":0}

	# get design_stories related to portfolio
	design_stories = DesignStory.objects.get_design_stories(username=username)

	story_ids = []
	cover_photos = []

	# get cover photos
	if design_stories != None:
		for story in design_stories:
			story_ids.append(story['design_story_id'])
			cover_photo = Entry.objects.get_cover_photos(story['design_story_id'])
			cover_photos.append(cover_photo)
		
		context['stories'] = zip(design_stories, cover_photos)
		context['num_pieces'] = len(design_stories)

	# get likes and follow
	if request.user.is_authenticated():

		# get following status
		context['is_following'] = Follow.objects.get_is_following(follower = request.user, followee = portfolio_data['user'])

		# get likes
		if design_stories != None:
			likes = Like.objects.get_likes(liker=request.user, story_ids=story_ids)
			context['likes'] = likes
		
	return render(request, "Portfolios/portfolio.html", context)

def render_design_story(request, username, story_id, slug):
	
	# get portfolio data
	column_list = ['user__first_name', 'user__last_name','avatar']
	portfolio_data = Designer.objects.get_portfolio_data(username = username, column_list = column_list)
	
	# get details of the specific design story
	design_story = DesignStory.objects.get_design_story(username=username, design_story_id=story_id)
	
	if design_story == None:
		raise Http404

	context = {
				"design_story": design_story, 
				"username":username,
				"design_story_id":story_id,
				"portfolio_data":portfolio_data,
				"slug": slug
			   }

	# get entries associated with story
	entries = Entry.objects.get_entries(story_id=story_id)

	if entries != None:
		context['entries'] = entries

	return render(request, "Portfolios/story.html", context)

######### WORK HERE
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
					rename(p,"%s/%s"%(bucket_link,i))
					i+=1

				return HttpResponseRedirect(reverse('Portfolios:render_design_story', args=(username, new_design_story.design_story_id, slug)))
			else:
				context['error'] = dict(design_story_form.errors.items() + entry_form.errors.items())
		else:

			# page is being "getted"
			context['entry_form']= CreateEntry(label_suffix='')
			context['design_story_form']= CreateDesignStory(label_suffix='')
			cl_init_js_callbacks(context['entry_form'], request)
		return render(request, "Portfolios/create_design_story.html",context)

	else:
		raise Http404

# work required....
@login_required
def create_chapter(request, username, story_id, slug):
	context = {}
	if request.user.username == username:
		if request.method =="POST":
			entry_form = CreateEntry(request.POST)
			if entry_form.is_valid():
				new_entry = entry_form.save(commit=False)
				new_entry.design_story_id = story_id
				new_entry.save()

				# update the bucket link
			 	bucket_link = "%s/%s/%s" % (username, story_id, new_entry.entry_id)
			 	new_entry.bucket_link = bucket_link
			 	new_entry.save()

				# rename photos pushed to cloudinary
				photos = request.POST.getlist('entry_photos')
				i = 0
				for photo in photos:
					p = photo.split("/")[3]
					p = p.split('#')[0].split('.')[0]
					rename(p,"%s/%s"%(bucket_link,i))
					i+=1

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
	
##############

@login_required
def edit_design_story(request, username):
	pass

@login_required
def like_design_story(request, username):
	if request.is_ajax():
		liker = request.POST['liker']
		design_story_id = request.POST['design_story_id']
		try:
			Like.objects.create(liker_id=liker, design_story_id=design_story_id)
		except:
			raise
	return HttpResponse(True)

@login_required
def unlike_design_story(request, username):
	if request.is_ajax():
		liker = request.POST['liker']
		design_story_id = request.POST['design_story_id']
		try:
			Like.objects.filter(liker_id=liker, design_story_id=design_story_id).delete()
		except:
			raise
	return HttpResponse(True)

@login_required
def follow_designer(request, username):
	if request.is_ajax():
		follower = request.POST['follower']
		followee = request.POST['followee']
		try:
			Follow.objects.create(follower_id=follower, followee_id=followee)
		except:
			raise
	return HttpResponse(True)

@login_required
def unfollow_designer(request, username):
	if request.is_ajax():
		follower = request.POST['follower']
		followee = request.POST['followee']
		try:
			Follow.objects.filter(follower=follower, followee=followee).delete()
		except:
			raise
	return HttpResponse(True)

@login_required
def comment(request, username):
	pass