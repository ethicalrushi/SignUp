from django.urls import path, include
from django.conf.urls import url
from loginapp import views
from loginapp.views import DisplayViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register('images',DisplayViewSet,'images')
app_name = 'loginapp'


urlpatterns = [
	url(r'^',include(router.urls)),
 
   
]