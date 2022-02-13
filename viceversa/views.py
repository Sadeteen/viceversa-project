from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	return HttpResponse('This page is about nothing')

def home(request):
	return render(request, 'home.html', {'greeting':'Hello!'})