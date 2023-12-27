from django.urls import path, include
from rest_framework import routers
from . import views
from . import api


routers = routers.DefaultRouter()
routers.register(r'api/data', api.DataTestAPI)

urlpatterns = [
	path('', views.index, name='home'),
	path('', include(routers.urls))
]
