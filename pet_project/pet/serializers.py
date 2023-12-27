from rest_framework import serializers
from .models import DataTest


class DataTestSerializer(serializers.ModelSerializer):
	class Meta:
		model = DataTest
		fields = '__all__'


