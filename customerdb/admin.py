from django.contrib import admin
from customerdb.models import Customer, Employee, Appointment, Car, Work
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Appointment)
admin.site.register(Car)
admin.site.register(Work)