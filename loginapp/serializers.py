from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

	image = serializers.ImageField(max_length=None,use_url=True)
	
	
	class Meta():
		model = User
		fields = ('username','fullname','image')


	
	