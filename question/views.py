from django.shortcuts import render #renderig all file handling work 

# Create your views here.

def all_questions(request):
	context= {'name':'Abhishek', 'phone':'9582135023'}#thde keys in dict will becom evariables in templates
	return render(request,'question/index.html',context)