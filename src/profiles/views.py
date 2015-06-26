from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
	context = {}
	template = 'home.html'
	return render(request, template, context)

def about(request):
	context = {}
	template = 'about.html'
	return render(request, template, context)

@login_required
def profile(request):
	user = request.user
	context = {'user': user}
	template = 'profile.html'
	return render(request, template, context)