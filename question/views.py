from django.shortcuts import render, get_object_or_404,redirect
 #renderig all file handling work 
from .models import Question
# Create your views here.
from django.http import Http404 , JsonResponse, HttpResponse
from django.views.decorators.http import require_GET,require_POST, require_http_methods	
from django.core import serializers	
from django.views.decorators.csrf import csrf_exempt
from .forms import QuestionCreateForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from account.urls import home

@csrf_exempt
def all_questions(request):
	context= {'q_list':Question.objects.all()}#the keys in dict will become variables in templates
	return render(request,'question/index.html',context)

@require_GET
def show_question_add_form(request):
	context = {'f': QuestionCreateForm() }
	return render(request,'question/create_form.html',context)

@require_http_methods(['GET', 'POST'])
@login_required
def add_question(request):
    if request.method == 'GET':
        f = QuestionCreateForm()
    else:
        f = QuestionCreateForm(request.POST)
        if f.is_valid():
            question_obj = f.save(commit = False)
            question_obj.created_by = request.user
            question_obj.save()
            return redirect(reverse('home',kwargs={'id': request.user.id}))
    return render(request, 'question/create_form.html', {'f': f})

@require_POST
def save_question(request):
	title = request.POST.get('title','')
	if not title:
		raise Http404

	q = Question.objects.create(title = title ,created_by = request.user)

	print(request.POST)
	return HttpResponse('ok')

@require_GET
@csrf_exempt	
def get_questions(request,id = None):
	# if request.method != 'GET':
	# 	raise Http404
	# this has been provided in a decorator
	if not id:
		raise Http404
	# try:
	# 	q = Question.objects.get(id=id)
	# except Question.DoesNotExist:
	# 	raise Http404
	q = get_object_or_404(Question,id=id) 

	data = serializers.serialize('json',[q])

	# data = {'id': q.id , 'title': q.title , 'text': q.text}
	
	return HttpResponse(data, content_type ='application/json')
