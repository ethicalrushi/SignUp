from django import forms
from loginapp.models import User
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta():
		model = User
		fields = ('username','password','fullname','image')