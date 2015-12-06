from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Customer(models.Model):
	first_name = models.CharField(max_length=100, blank=True)
	last_name = models.CharField(max_length=100, blank=True)
	email = models.CharField(max_length=100, blank=True)
	phone = models.CharField(max_length=10, blank = True)
	street = models.CharField(max_length=50, blank=True)
	city = models.CharField(max_length=40, blank=True)
	state = models.CharField(max_length=40, blank=True)
	zip_code = models.CharField(max_length=5, blank = True)
	
	def __unicode__(self):
		return self.first_name

class Car(models.Model):
	make = models.CharField(max_length=100, blank=True)
	model = models.CharField(max_length=100, blank=True)
	year = models.CharField(max_length=100, blank=True)
	plate = models.CharField(max_length=100, blank=True)
	vin = models.CharField(max_length=100, blank=True)
	customer = models.ForeignKey('Customer', default=False)

	def __unicode__(self):
		return (self.year + " " + self.model + " "+ self.make)


class Employee(models.Model):
	first_name = models.CharField(max_length=100, blank=True)
	last_name = models.CharField(max_length=100, blank=True)
	email = models.CharField(max_length=100, blank=True)
	phone = models.CharField(max_length=10, blank = True)
	
	def __unicode__(self):
		return (self.first_name + "<>")

class Appointment(models.Model):
	customer = models.ForeignKey(Customer)
	employee = models.ForeignKey(Employee)
	car = models.ForeignKey(Car, blank=True)
	date = models.DateTimeField(auto_now_add=True, blank=True)


class Work(models.Model):
	type_of_work = models.CharField(max_length=100, blank=True)
	cost = models.CharField(max_length=100, blank=True)
	appointment = models.ForeignKey(Appointment, blank=True)

	