from django.shortcuts import render
from .forms import UserForm
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login,logout

# Create your views here.
def register(request):
	form = UserForm()
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			password = form.cleaned_data['password']
			print(password)
			user = User()
			user.password = make_password(password)
			user.username = form.cleaned_data['username']
			user.save()
			print(user.password)
			
		else:
			print(error)
	else:
		return render(request,'register.html',{'form':form,})

	return render(request,'register.html',{'form':form,})


def loginview(request):
	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		userpass= User.objects.get(username=username).password
		user = User.objects.get(username=username)
		if check_password(password, userpass):
			print('wow')
			login(request,user)

	return render(request,'login.html')	 

		