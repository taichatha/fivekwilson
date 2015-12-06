from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.db import models
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from customerdb.forms import UserForm, CustomerForm, EmployeeForm, AppointmentUserForm, CarForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from customerdb.models import Customer, Employee, Appointment, Car, Work
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

def add_workorder(request, customer_id):
	customer = get_object_or_404(Customer, pk=customer_id)
	employee = get_object_or_404(Employee, pk= 1)
	appointment_user_form = request.POST
	appointment = Appointment(customer=customer, employee=employee)
	number = 0
	
	if request.method == 'POST':
		car = get_object_or_404(Car, pk=request.POST.get('car_id'))
		appointment.car = car
		appointment.save()
		print request.POST.get('number')
		print
		for i in range(0, int(request.POST.get('number'))+1):
			print('work'+str(i))
			work = Work(type_of_work= request.POST.get('work'+str(i)), cost=request.POST.get('cost'+str(i)), appointment=appointment)
			work.save()
			print work.type_of_work

		

		return HttpResponseRedirect('/customerdb/'+ customer_id+"/")

	else:
		appointment_user_form = AppointmentUserForm()


	return render(request, 'customerdb/create_workorder.html', {'appointment_user_form': appointment_user_form, 'customer': customer, 'number':number})

def delete_workorder(request, appointment_id, customer_id):
	appt = get_object_or_404(Appointment, pk=appointment_id)
	appt.delete()

	return HttpResponseRedirect('/customerdb/'+ customer_id+"/")


def add_car(request, customer_id):
	context = RequestContext(request)
	customer = get_object_or_404(Customer, pk=customer_id)
	redirect_to = request.REQUEST.get('next', '')
	if request.method == 'POST':
		car_form = CarForm(data=request.POST)

		if car_form.is_valid():
			car = car_form.save(commit=False)
			car.customer = customer 
			car.save()
			return HttpResponseRedirect(redirect_to)
		
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
