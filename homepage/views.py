from django.shortcuts import render_to_response
from django.http import HttpResponse

def homepage_view(request):
	return render_to_response('homepage.html',
							 {'name': 'bob'}
	)

def welcome_view(request):
	return HttpResponse('Welcome')