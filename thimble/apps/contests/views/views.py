from django.shortcuts import render
from django.core.context_processors import csrf

def contests(request):
	return render(request, 'contests/<template_name>',{})

def shirts(request):
	return render(request,'contests/<template_name>',{})

