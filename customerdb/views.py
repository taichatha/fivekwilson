from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.db import models
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from customerdb.forms import UserForm, CustomerForm, EmployeeForm, AppointmentForm, CarForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from customerdb.models import Customer, Employee, Appointment, Car
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.
def index(request):
	return render(request, 'customerdb/index.html')


def show_customers(request):
	#must be employee, must be admin, must be user
	customers = Customer.objects.all()
	return render(request, 'customerdb/show_customers.html', {'customers': customers})


def customer_profile(request, customer_id):
	#must be employee, must be admin
	#must be customer_id
	customer = get_object_or_404(Customer, pk=customer_id)

	return render(request, 'customerdb/customer_profile.html', {'customer': customer})


def add_car(request, customer_id):
	context = RequestContext(request)
	customer = get_object_or_404(Customer, pk=customer_id)
	if request.method == 'POST':
		car_form = CarForm(data=request.POST)

		if car_form.is_valid():
			car = car_form.save(commit=False)
			car.customer = customer 
			car.save()
			return HttpResponseRedirect('/customerdb/'+ customer_id+"/")
		
	else:
		car_form = CarForm()

	return render(request, 'customerdb/add_car.html', {'car_form': car_form, 'customer': customer})

def delete_car(request, car_id, customer_id):
	car = get_object_or_404(Car, pk=car_id)
	car.delete()

	return HttpResponseRedirect('/customerdb/'+ customer_id+"/")


def create_customer(request):
	#must be employee, must be admin
	context = RequestContext(request)

	if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
	    customer_form = CustomerForm(data=request.POST)
	    customers = Customer.objects.all()

	    # If the two forms are valid...
	    if customer_form.is_valid():
	        customer = customer_form.save(commit=False)
	        empty = 0
	        
	        for i in customers:
	        	if i.first_name == customer.first_name and i.last_name == customer.last_name:
	        		empty+=1
	        		# print i.id 

	        if empty == 0:
		        customer.save()
		        return HttpResponseRedirect('/customerdb')

		    
	    else:
	    	print customer_form.errors

	else:
	    customer_form = CustomerForm()

	return render(request, 'customerdb/create_customer.html', {'customer_form': customer_form})
