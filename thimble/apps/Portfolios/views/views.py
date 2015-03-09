from django.shortcuts import render
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
from thimble.apps.Users.models.schemas.Designer import Designer

# forms 
from thimble.apps.Portfolios.forms.create_forms import *


# figure out how to clear session in an appropriate manner (Salil Gupta)

def render_portfolio(request, subdomain, isEditMode=False):
	portfolio_data = Designer.objects.get_portfolio_data(subdomain=subdomain)

	# if portfolio isn't real then raise error
	if portfolio_data == None:
		raise Http404

	context = {"subdomain":subdomain,"portfolio_data":portfolio_data, "isEditMode":isEditMode}

	# get design_stories related to portfolio
	design_stories = DesignStory.objects.get_design_stories(subdomain=subdomain)

	if design_stories != None:
		context['design_stories'] = design_stories
		context['cover_photos'] = []
		for design_story in design_stories:
			cover_photo = Entry.objects.get_cover_photos(design_story['design_story_id'])[0]
			context['cover_photos'].append(cover_photo)

		context['stories'] = zip(context['design_stories'],context['cover_photos'])
		del context['cover_photos']
		del context['design_stories']
	
	# fix to clear out sessions when a different designer is uploaded
	# will cause a bug fix later (Salil Gupta)

	request.session['designer_name'] = portfolio_data.user.first_name +" "+ portfolio_data.user.last_name
	request.session['prof_pic'] = portfolio_data.prof_pic.public_id

	return render(request, "Portfolios/%s.html" % portfolio_data.template_theme, context)

def render_design_story(request,subdomain,story_id):

	# get details of the specific design story
	design_story = DesignStory.objects.get_design_story(subdomain=subdomain, design_story_id=story_id)
	
	if design_story == None:
		raise Http404

	context = {"design_story": design_story}

	# get entries associated with story
	entries = Entry.objects.get_entries(story_id=story_id)

	if entries !=None:
		context['entries'] = entries

	context['subdomain'] = subdomain

	return render(request, "Portfolios/story.html", context)


@login_required
def edit_portfolio(request, subdomain):
	# user must be logged in and must be accessing personal portfolio
	# not someone else's
	if request.user.designer.subdomain == subdomain:
		return render_portfolio(request, subdomain, True)
	else:
		raise Http404

@login_required 
def create_design_story(request, subdomain):
	if request.user.designer.subdomain == subdomain:
		context = {'subdomain':subdomain}
		if request.method == "POST":
			# form is posted
			design_story_form = DesignStoryForm(request.POST)
			entry_form = EntryForm(request.POST)

			if design_story_form.is_valid() and entry_form.is_valid():

				# create an instance of the of design_story_model model
				new_design_story = design_story_form.save(commit=False)
				new_design_story.designer = request.user.designer
				new_design_story.save()

				# create an instance of the entry model
				new_entry = entry_form.save(commit=False)
				new_entry.design_story = new_design_story
				new_entry.save()

				e_id = new_entry.entry_id
				
				# update the bucket link
				bucket_link = "%s/%s/%s" % (subdomain, new_design_story.design_story_id,e_id)
				new_entry.bucket_link  = bucket_link
				new_entry.save()

				# rename photos pushed to cloudinary
				photos = request.POST.getlist('entry_photos')
				i = 0
				for photo in photos:
					p = photo.split("/")[3]
					p = p.split('#')[0].split('.')[0]
					rename(p,"%s/%s"%(bucket_link,i))
					i+=1

				return HttpResponseRedirect(reverse('Portfolios:render_design_story', args=(subdomain, new_design_story.pk)))
			else:
				context['error'] = dict(design_story_form.errors.items() + entry_form.errors.items())
		else:
			# page is being "getted"
			design_story_form = DesignStoryForm()
			entry_form = EntryForm()
			context['entry_form']=entry_form
			context['design_story_form']=design_story_form
			cl_init_js_callbacks(context['entry_form'], request)
		return render(request, "Portfolios/create_design_story.html",context)

	else:
		raise Http404
