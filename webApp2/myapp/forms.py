from django.forms import ModelForm
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


