from django.contrib import admin
from customerdb.models import Customer, Employee, Appointment
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Appointment)