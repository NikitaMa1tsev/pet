from django.shortcuts import render, HttpResponse

from .models import DataTest

def index(request):
	return render(request, 'pet/index.html')




