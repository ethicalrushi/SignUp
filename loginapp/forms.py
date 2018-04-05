from django import forms
from loginapp.models import User
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta():
		model = User
		fields = '__all__'