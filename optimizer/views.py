from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
	return HttpResponse('hey')

# assume one recipe
def get_total_cost(resource):
	pass
	# Recipe.get(resource.filter()
