from django.shortcuts import render
from django.http import Http404
from thimble.apps.Portfolios.models.schemas.DesignStory import DesignStory
from thimble.apps.Users.models.schemas.Designer import Designer

# Cloudinary stuff
from django import forms
from django.http import HttpResponse

from cloudinary.forms import cl_init_js_callbacks      
#from thimble.apps.Portfolios.models.schemas.Photo import Photo
#from thimble.apps.Portfolios.forms import PhotoDirectForm
import json      
from django import forms
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt      


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


# def image_upload(request, subdomain):
# 	return render(request, "Portfolios/image_upload.html", {})


# def upload_prompt(request, subdomain):
#   context = dict(direct_form = PhotoDirectForm())
#   cl_init_js_callbacks(context['direct_form'], request)
#   return render(request, 'Portfolios/upload_prompt.html', context)

  

@csrf_exempt
def direct_upload_complete(request, subdomain):
  form = PhotoDirectForm(request.POST)
  if form.is_valid():
    form.save()
    ret = dict(photo_id = form.instance.id)
  else:
    ret = dict(errors = form.errors)
    
  return HttpResponse(json.dumps(ret), content_type='application/json')