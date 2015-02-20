from django.shortcuts import render
from django.http import Http404
from thimble.apps.Portfolios.models.schemas.DesignStory import DesignStory
from thimble.apps.Users.models.schemas.Designer import Designer
# Create your views here.

def render_portfolio(request, subdomain):
	portfolio_data = Designer.objects.get_portfolio_data(subdomain)

	if portfolio_data == None:
		raise Http404

	design_stories = DesignStory.objects.get_design_stories(designer_id=portfolio_data[0])

	if design_stories == None:
		context = {}
	else:
		context = {"design_stories":design_stories}

	# load whatever theme the portfolio is .. 
	return render(request, "Portfolios/%s.html" % portfolio_data[1], context)

def edit_portfolio(request, subdomain):
	pass