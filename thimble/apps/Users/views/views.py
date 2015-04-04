from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required

from thimble.apps.Users.forms.forms import *
from thimble.apps.Users.models.schemas.Designer import Designer

from cloudinary.forms import cl_init_js_callbacks


# look into Dangling orphans (Salil Gupta)
def create_account(request):
	context = {}
	if request.method == "POST":
		user_form = RegistrationForm(request.POST)
		if user_form.is_valid():

			# create an instance of the user model
			new_user = user_form.save()

			# create a designer instance
			designer = Designer.objects.create(user=new_user)

			# login user after account is created  
			user = authenticate(username=user_form.cleaned_data['username'], password=user_form.cleaned_data['password1'])
			login(request,user)

			# send them to edit their profile
			return HttpResponseRedirect(reverse('Users:edit_account'))
		else:
			context['error'] = dict(user_form.errors.items())
	else:
		user_form = RegistrationForm()
		context = {'user_form':user_form}

	return render(request, "Users/create_account.html", context)

# Work on error handling (Salil Gupta)
# provide user feedback on Image upload being complete (Salil Gupta)
@login_required 
def edit_account(request):
	context = {}
	if request.method=="POST":
		# receiving form data
		edit_user = EditUserForm(request.POST, instance=request.user)
		edit_designer = EditDesignerForm(request.POST, instance = request.user.designer)

		if edit_user.is_valid() and edit_designer.is_valid():
			# save forms if valid
			updated_user = edit_user.save()
			updated_designer = edit_designer.save()
		else:
			context['error'] = "error"
	else:
		# create forms for displaying
		edit_user = EditUserForm(instance=request.user)
		edit_designer = EditDesignerForm(instance = request.user.designer)

	context['edit_user'] = edit_user
	context['edit_designer'] = edit_designer
	return render(request, "Users/edit_account.html", context)
