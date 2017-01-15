from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 , redirect
from django.http import Http404 , JsonResponse, HttpResponse
from django.views.decorators.http import require_GET,require_POST, require_http_methods	
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate , logout as auth_logout, login as auth_login
from django.core.urlresolvers import reverse

# Create your views here.

def hello(request):
	#print(request.GET['abc'])#never directly use [] with request
	# print(request.GET.get('abc'))#it doesnt give error if abc doesnt exist,instead return none
	# print(request.session)
	# print(request.user)
	return HttpResponse('<h1>hello</h1>')

@require_GET
def show_login(request):
	if request.user.is_authenticated():
		return redirect('/account/home')
	return render(request, 'account/auth/login.html')

@require_POST
def login(request):
	if request.user.is_authenticated():
		return redirect(reverse('home',kwargs={'id': request.user.id}))

	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = authenticate(username = username,password = password)
	if not user:
		context = {'error': 'Invalid username/paswword'}
		return render(request, 'account/auth/login.html',context)
	else:
		auth_login(request,user) #inbuild handling of sessions .
		return redirect(reverse('home',kwargs={'id': request.user.id}))   

def home(request,id):
	if not request.user.is_authenticated():
		return redirect(reverse('base'))
	return render(request,'account/auth/loggedin.html')

def logout(request):
	auth_logout(request)
	return redirect(reverse('base'))
