from django.shortcuts import render #renderig all file handling work 
from .models import Question
# Create your views here.
from django.http import Http404 , JsonResponse
	

def all_questions(request):
	context= {'q_list':Question.objects.all()}#the keys in dict will become variables in templates
	return render(request,'question/index.html',context)

def get_questions(request,id = None):
	if not id:
		raise Http404;
	try:
		q = Question.objects.get(id=id)
	except Question.DoesNotExist:
		raise Http404

	data = {'id': q.id , 'title': q.title , 'text': q.text}
	
	return JsonResponse(data)
