from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from thimble.apps.Users.forms.registration_forms import *

from cloudinary.forms import cl_init_js_callbacks


def create_account(request):

	# userForm = RegistrationForm()
	# designerForm = DesignerRegistrationForm()
	# context = dict(
	# 	user_form = userForm,
	# 	designer_form = designerForm
	# )

	direct_form = PhotoDirectForm()
	context = dict(
		direct_form = direct_form,
	)
	# When using direct upload - the following call in necessary to update the form's callback url cl_init_js_callbacks(context['designer_form'], request)
	cl_init_js_callbacks(context['direct_form'], request)

	return render(request, "Users/create_account.html", context)

@csrf_exempt
def direct_upload_complete(request):
	form = PhotoDirectForm(request.POST)
	if form.is_valid():
		# Create a model instance for uploaded image using the provided data
		form.save()
	else:
		print form.errors

	return HttpResponseRedirect(reverse('landingpage:landingpage'))


# @csrf_exempt
# def direct_upload_complete(request):
# 	userForm = RegistrationForm(request.POST)
# 	designerForm = DesignerRegistrationForm(request.POST)

# 	if userForm.is_valid() and designerForm.is_valid():
# 		new_user = userForm.save()
# 		new_designer = designerForm.save(commit=False)
# 		new_designer.user = new_user
# 		new_designer.save()
# 		print new_designer.user.username #success
# 		print new_designer.prof_pic # this is null
# 	else:
# 		print "invalid form data"
	
# 	return HttpResponseRedirect(reverse('landingpage:landingpage'))
