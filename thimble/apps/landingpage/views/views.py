from django.shortcuts import render
from django.core.context_processors import csrf
import mailchimp, os

def landingpage(request):
	context = {}
	if request.method=="POST":
		email = request.POST.get('email')
		api = mailchimp.Mailchimp(os.environ['MAILCHIMP_API_KEY'])
		result = api.lists.subscribe(os.environ['MAILCHIMP_LIST_ID'], {'email':email})
		if 'error' in result:
			context['error'] = result['error']
		else:
			context['success'] = "Thanks for subscribing to Thimble!"
	return render(request, "landingpage/index.html",context)
