from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

from thimble.apps.Users.forms.registration_forms import *

def create_account(request):
	if request.method == 'POST':
		userForm = RegistrationForm(request.POST)
		DesignerForm = DesignerRegistrationForm(request.POST)
		if userForm.is_valid() and DesignerForm.is_valid():
			new_user = userForm.save()
			new_designer = DesignerForm.save(commit=False)
			new_designer.user = new_user
			new_designer.save()		
		return render(request, "landingpage/index.html", {})
	else:	
		userForm = RegistrationForm()
		DesignerForm = DesignerRegistrationForm()
		context = {}
		context["reg_form"] = userForm
		context["form"] = DesignerForm
		return render(request, "Users/create_account.html", context)
