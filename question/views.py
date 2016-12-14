from django.shortcuts import render, get_object_or_404
 #renderig all file handling work 
from .models import Question
# Create your views here.
from django.http import Http404 , JsonResponse, HttpResponse
from django.core import serializers	

def all_questions(request):
	context= {'q_list':Question.objects.all()}#the keys in dict will become variables in templates
	return render(request,'question/index.html',context)

def get_questions(request,id = None):
	if not id:
		raise Http404;

	# try:
	# 	q = Question.objects.get(id=id)
	# except Question.DoesNotExist:
	# 	raise Http404
	q = get_object_or_404(Question,id=id) 

	data = serializers.serialize('json',[q])

	# data = {'id': q.id , 'title': q.title , 'text': q.text}
	
	return HttpResponse(data, content_type ='application/json')
