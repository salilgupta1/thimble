from django.shortcuts import render
from django.core.context_processors import csrf

def contests(request):
	return render(request, 'contests/contests.html',{})

def shirts(request):
	return render(request,'contests/vote.html',{})

def results(request):
	return render(request,'contests/results.html',{})

def shop(request):
	return render(request,'contests/shop.html',{})
