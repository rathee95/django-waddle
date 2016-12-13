from django.shortcuts import render #renderig all file handling work 
from .models import Question
# Create your views here.

def all_questions(request):
	context= {'q_list':Question.objects.all()}#the keys in dict will become variables in templates
	return render(request,'question/index.html',context)