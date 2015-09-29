from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.db import models
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from customerdb.forms import UserForm, CustomerForm, EmployeeForm, AppointmentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from customerdb.models import Customer, Employee, Appointment
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.
def index(request):
	return render(request, 'customerdb/index.html')

def create_customer(request):
	context = RequestContext(request)

	if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
	    customer_form = CustomerForm(data=request.POST)

	    # If the two forms are valid...
	    if customer_form.is_valid():
	        customer = customer_form.save(commit=False)
	        
	        # Now we save the UserProfile model instance.
	        customer.save()

	        # Update our variable to tell the template registration was successful.
	        

	    # Invalid form or forms - mistakes or something else?
	    # Print problems to the terminal.
	    # They'll also be shown to the user.
	    else:
	    	print customer_form.errors

	else:
	    customer_form = CustomerForm()

	return render(request, 'customerdb/create_customer.html', {'customer_form': customer_form})
