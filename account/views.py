from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
	#print(request.GET['abc'])#never directly use [] with request
	# print(request.GET.get('abc'))#it doesnt give error if abc doesnt exist,instead return none
	# print(request.session)
	# print(request.user)
	return HttpResponse('<h1>hello</h1>')


