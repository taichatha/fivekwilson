from customerdb.models import Customer, Employee, Appointment, Car
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelChoiceField
 # As the name of the nested class may suggest,
 # anything within a nested Meta class describes
 # additional properties about the particular
 # ModelForm class it belongs to.

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class CarForm(forms.ModelForm):
    class Meta:
        model = Car 
        fields = ('make', 'model', 'year', 'plate', 'vin')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'phone', 'street', 'city', 'state', 'zip_code')
    
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name','last_name')

class AppointmentForm(forms.Form):
    class Meta:
        model = Appointment
        fields = ('customer', 'employee', 'date')
