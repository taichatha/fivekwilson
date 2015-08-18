from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Customer(models.Model):
	user = models.OneToOneField(User, related_name = "Customer")
	phone = models.CharField(max_length=10, blank = True)
	street = models.CharField(max_length=50, blank=True)
	city = models.CharField(max_length=40, blank=True)
	state = models.CharField(max_length=40, blank=True)
	zip_code = models.CharField(max_length=5, blank = True)
	
	def __unicode__(self):
		return self.user.first_name

class Employee(models.Model):
	user = models.OneToOneField(User, related_name = "Employee")

	def __unicode__(self):
		return self.user.first_name

class Appointment(models.Model):
	customer = models.ForeignKey(Customer)
	employee = models.ForeignKey(Employee)
	date = models.DateTimeField('Date of Appointment', blank=True)