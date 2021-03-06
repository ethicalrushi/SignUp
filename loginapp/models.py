from django.db import models
import uuid
# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=200, unique=True)
	password = models.CharField(max_length=200)
	user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
	fullname = models.CharField(max_length=200, blank=True,null=True)
	image = models.ImageField(upload_to='image', blank=True, null=True)
  
   


	def __str__(self):
		return self.username
		