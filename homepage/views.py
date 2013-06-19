from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse

def homepage_view(request):
	return render_to_response('homepage.html',
							 {'name': 'bob'}
							 )

def welcome_view(request):
	return HttpResponse('Welcome')

def form_view(request):
	return render(request, 'form.html')

def form_handler(request):
	return HttpResponse('got it! %s' % request.GET['name'])