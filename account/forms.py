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
	def __init__(self,*args,**kwargs):
		self.authenticated_user = None;
		super(LoginForm,self).__init__(*args,**kwargs);
	def clean_username(self):
		data_username = self.cleaned_data['username']
		if MyUser.objects.filter(username = data_username).count() != 1:
			raise forms.ValidationError('Invalid Username')
		return data_username
	#this runs for multiple fields and their dependency .
	#check username matches with password here 
	def clean(self):
		data_username = self.cleaned_data.get('username','')
		data_password = self.cleaned_data.get('password','')
		user = authenticate(username = data_username,password = data_password)
		if (data_username and data_password and not user):
			raise forms.ValidationError('username and password does not match')
		# on success return the full dictionary !! 
		self.authenticated_user = user
		return self.cleaned_data


class ForgetPassword(forms.Form):
	username = forms.CharField(max_length = 100)

	def clean_username(self):
		data_username =self.cleaned_data.get('username','')
		if data_username and not	MyUser.objects.filter(username = data_username).exists():
			raise forms.ValidationError('Invalid username') 
		return data_username  