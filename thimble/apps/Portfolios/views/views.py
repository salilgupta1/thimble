from django.shortcuts import render
from django.http import Http404

from thimble.apps.Portfolios.models.schemas.Entry import Entry
from thimble.apps.Portfolios.models.schemas.DesignStory import DesignStory
from thimble.apps.Users.models.schemas.Designer import Designer

# figure out how to clear session in an appropriate manner (Salil Gupta)

def render_portfolio(request, subdomain):
	# get portfolio data
	portfolio_data = Designer.objects.get_portfolio_data(subdomain=subdomain)

	# if portfolio isn't real then raise error
	if portfolio_data == None:
		raise Http404

	context = {"subdomain":subdomain,"portfolio_data":portfolio_data}
	print portfolio_data.prof_pic
	# get design_stories related to portfolio
	design_stories = DesignStory.objects.get_design_stories(subdomain=subdomain)

	if design_stories != None:
		context['design_stories'] = design_stories

	# save meta data for later
	request.session['designer_name'] = portfolio_data.user.first_name +" "+ portfolio_data.user.last_name
	request.session['prof_pic'] = portfolio_data.prof_pic.public_id

	return render(request, "Portfolios/%s.html" % portfolio_data.template_theme, context)


def render_design_story(request,subdomain,story_id):

	# get details of the specific design story
	design_story = DesignStory.objects.get_design_story(subdomain=subdomain, design_story_id=story_id)
	print request.session['designer_name']
	if design_story == None:
		raise Http404

	context = {"design_story": design_story}

	# get entries associated with story
	entries = Entry.objects.get_entries(story_id=story_id)

	if entries !=None:
		context['entries'] = entries

	return render(request, "Portfolios/story.html", context)

def edit_portfolio(request, subdomain):
	pass