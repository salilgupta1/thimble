from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth import authenticate, login

from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from thimble.apps.Users.forms.registration_forms import *

from cloudinary.forms import cl_init_js_callbacks


def create_account(request):

	context = {}
	if request.method == "POST":
		user_form = RegistrationForm(request.POST)
		designer_form = DesignerRegistrationForm(request.POST)

		if user_form.is_valid() and designer_form.is_valid():
			# create an instance of the user model
			new_user = user_form.save()

			# create an instance of the designer model
			new_designer = designer_form.save(commit=False)

			# attach the user to the designer model
			new_designer.user = new_user
			new_designer.save()

			# login user after account is created  
			user = authenticate(new_user.username, new_user.password)
			login(request,user)

			# send them to edit their profile
			return HttpResponseRedirect(reverse('Portfolios:edit_portfolio', args=(request.POST['subdomain'],)))
		else:
			context['error'] = dict(user_form.errors.items() + designer_form.errors.items())
	else:
		user_form = RegistrationForm()
		designer_form = DesignerRegistrationForm()
		context = {'user_form':user_form,'designer_form':designer_form}
		cl_init_js_callbacks(context['designer_form'], request)

	return render(request, "Users/create_account.html", context)

