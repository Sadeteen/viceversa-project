from django.http import HttpResponse
from django.shortcuts import render

def about(request):
	return HttpResponse('This page is about nothing')

def home(request):
	return render(request, 'home.html', {'greeting':'Hello!'})

def reverse(request):
	user_text = request.GET['usertext']
	reversed_user_text = user_text[::-1]
	return render(request, 'reverse.html', {'usertext':user_text, 'reversed_usertext':reversed_user_text})

