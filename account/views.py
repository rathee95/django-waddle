from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404 , redirect
from django.http import Http404 , JsonResponse, HttpResponse
from django.views.decorators.http import require_GET,require_POST, require_http_methods	
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate , logout as auth_logout, login as auth_login
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, ForgetPassword
from .models import MyUser, create_otp, get_valid_otp_object
# Create your views here.
import inspect
from datetime import datetime, timedelta
from django.utils import timezone

def hello(request):
	#print(request.GET['abc'])#never directly use [] with request
	# print(request.GET.get('abc'))#it doesnt give error if abc doesnt exist,instead return none
	# print(request.session)
	# print(request.user)
	return HttpResponse('<h1>hello</h1>')

@require_http_methods(['GET','POST'])
def login(request):
	if request.user.is_authenticated():
		return redirect(reverse('home',kwargs={'id': request.user.id}))

	if request.method == 'GET':
		context = {'f': LoginForm() }
		return render(request, 'account/auth/login.html',context)
	else:		
		f = LoginForm(request.POST)
		if not f.is_valid(): #the constraint mentioned in form class are checked, field and non field errors are checked	
			return render(request,'account/auth/login.html',{'f':f} )
		else:
			user = f.authenticated_user
			auth_login(request,user)
			return redirect(reverse('home',kwargs={'id': user.id}))   


def forget_password(request):
	if request.user.is_authenticated():
		return redirect(reverse('home',kwargs={'id': request.user.id}))

	if request.method == 'GET':
		context = {'f': ForgetPassword() }
		return render(request, 'account/auth/forgot_password.html',context)
	else:		
		f = ForgetPassword(request.POST)
		if not f.is_valid(): #the constraint mentioned in form class are checked, field and non field errors are checked	
			return render(request,'account/auth/forgot_password.html',{'f':f} )
		else:
			user = MyUser.objects.get(username = f.cleaned_data['username']) 
			otp = create_otp(user = user ,purpose = 'FP')
			#SEND EMAIL <<<<<<<<<<<<< -------------------->>>>
			return render(request,'account/auth/forgot_email_sent.html',{'u':user}) 	


def reset_password(request, id = None, otp = None):
	if request.user.is_authenticated():
		return redirect(reverse('home',kwargs={'id': request.user.id}))
	
	user = get_object_or_404(MyUser,id= id)
	otp_object = get_valid_otp_object(user= user, purpose = 'FP',otp = otp )
	if not otp_object:
		raise Http404()

	
	# if request.method == 'GET':
	# 	context = {'f': LoginForm() }
	# 	return render(request, 'account/auth/login.html',context)
	# else:		
	# 	f = LoginForm(request.POST)
	# 	if not f.is_valid(): #the constraint mentioned in form class are checked, field and non field errors are checked	
	# 		return render(request,'account/auth/login.html',{'f':f} )
	# 	else:
	# 		user = f.authenticated_user
	# 		auth_login(request,user)


@require_GET
@login_required
def home(request,id):
	return render(request,'account/auth/loggedin.html')

def logout(request):
	auth_logout(request)
	return redirect(reverse('login'))

def all_users(request):
	print (inspect.stack()[0][3])
	list_user = MyUser.objects.all();

	print (list_user)
	how_many_days = 30
	list_user2 = MyUser.objects.values('username','id').order_by('date_joined').reverse()[:1]
	print (list_user2)
	a = 'account/auth/'+ inspect.stack()[0][3]+'.html'
	return render(request,a,{'u':list_user})