from django.shortcuts import render
from .forms import UserForm
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login,logout, authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer
from rest_framework.generics import RetrieveAPIView
from django.http import JsonResponse
from rest_framework.renderers import TemplateHTMLRenderer
import json
from django.views.generic.base import View
from django.urls import resolve

# Create your view
def register(request):

	form = UserForm()
	if request.method == 'POST':
		form = UserForm(request.POST, request.FILES)
		if form.is_valid():
			password = form.cleaned_data['password']

			print(password)
			user = User()
			user.password = make_password(password)
			user.username = form.cleaned_data['username']
			#user.profile_pic = form.cleaned_data['profile_pic']
			user.save()

			print(user.password)
			
		else:
			print(error)
	else:
		return render(request,'register.html',{'form':form,})
	#else:
		#return HttpResponse('Loginkaro')

	return render(request,'register.html',{'form':form,})


def loginview(request):
	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = User.objects.get(username=request.POST['username'])
		userpass= user.password
		
		if check_password(password, userpass):
			print('wow')
			request.session['username']= user.username
			return render(request,'index.html',{'username':username,})	 
	return render(request,'login.html')	
			
def index(request):
	return render(request,'index.html')
	


def logout(request):
	try:
		del request.session['username']
	except KeyError:
		pass
	return HttpResponse("logged out")


class UserList(APIView):

	def get(self,request):
		users = User.objects.all()
		serializer = UserSerializer(users, many=True)
		return Response(serializer.data)


