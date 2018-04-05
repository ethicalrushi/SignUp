from django.contrib import admin

# Register your models here.
from loginapp.models import User

admin.site.register(User)
