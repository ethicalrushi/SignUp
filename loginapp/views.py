from django.shortcuts import render
from .forms import UserForm
from .models import User
from django.contrib.auth.hashers import make_password, check_password

from django.http import HttpResponse


from rest_framework.response import Response
from rest_framework import status, viewsets

from .serializers import UserSerializer

from django.http import JsonResponse

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
			user.fullname = form.cleaned_data['fullname']
			user.image = form.cleaned_data['image']
			user.save()

			print(user.password)
			
		else:

			print(form.errors)
			return render(request,'register.html',{'form':form,})
	else:
		return render(request,'register.html',{'form':form,})
	

	return render(request,'register.html',{'form':form,})



	






class DisplayViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class= UserSerializer





def dataview(request):
	return render(request,'data.html')