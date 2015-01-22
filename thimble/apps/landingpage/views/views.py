from django.shortcuts import render
from django.core.context_processors import csrf
import os
import chimpy


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

	return render(request, "landingpage/index.html",context)
