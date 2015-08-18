from django.shortcuts import render, render_to_response, get_object_or_404
from django.db import models
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def index(request):

	return render(request, 'station/index.html')

def contact(request):

	return render(request, 'station/contact.html')