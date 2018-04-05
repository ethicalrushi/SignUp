from django import forms
from loginapp.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError









class UserForm(forms.ModelForm):
	username= forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta():
		model = User
		fields = ('username','password','fullname','image')


#def check_for_same(value):
	
	#if User.objects.filter(username=value).exists():
	#	raise form.ValidationError("Username is already used")

class FormLogin(forms.Form):
	username= forms.CharField(label=("Username"), required=True)
	password= forms.CharField(label=("Password"), widget=forms.PasswordInput,required=True)



def session_demo(request):
	username=None #default
	form_login = FormLogin()
	if request.method=='GET':
		if 'action' in request.GET:
			action= request.GET.get('action')
			if action == 'logout':
				if request.session.has_key('username'):
					request.session.flush()
				return redirect('demos-sessions')

		if 'username' in request.session:
			username= request.session['username']
	elif request.method=='POST':
		form_login= FormLogin(request.POST)
		if form_login.is_valid():
			username= form_login.cleaned_data['username']
			password= form_login.cleaned_data['password']
			user = User.objects.get(username=request.POST['username'])
			userpass= user.password
			if check_password(password, userpass):
				print('wow')
				request.session['username']= username
			else:
				username=None
	return render(request,'session.html',{'form':form_login,'username':username,})
