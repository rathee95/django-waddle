from django import forms
from account.models import MyUser
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
	username = forms.CharField(max_length = 25)
	password = forms.CharField(widget = forms.PasswordInput)
	#clean_ are called by itself on is_valid() call
	#cleaned_data ----> dict key:value
	#validation logic is shifted inside the form 
	#this is field error  ----->  clean_fieldname
	def clean_username(self):
		username = self.cleaned_data['username']
		if MyUser.objects.filter(username = username).count() != 1:
			raise forms.ValidationError('Invalid Username')
		return username
	#this runs for multiple fields and their dependency .
	#check username matches with password here 
	def clean(self):
		username = self.cleaned_data.get('username','')
		password = self.cleaned_data.get('password','')
		if username and password and not authenticate(username = username,password = password):
			raise forms.ValidationError('username and password does not match')
		# on success return the full dictionary !! 
		return self.cleaned_data


