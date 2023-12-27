from rest_framework import viewsets

from .models import DataTest
from .serializers import DataTestSerializer


class DataTestAPI(viewsets.ModelViewSet):
	queryset = DataTest.objects.all()
	serializer_class = DataTestSerializer
	# http_method_names = ['get']
