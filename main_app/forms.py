from django.forms import ModelForm, Form, CharField, PasswordInput
from .models import Trail, Hiker, Trip
from django import forms

class LoginForm(Form):
    username = CharField(label="User Name", max_length=64)
    password = CharField(widget=PasswordInput())

class TrailForm(ModelForm):
    model = Trail
    fields = ['name', 'length', 'difficulty', 'location']

class HikerForm(ModelForm):
    model = Hiker
    fields = ['first_name', 'sex', 'age', 'experience', 'email']

class TripForm(ModelForm):
    model = Trip
    fields = ['trail', 'date', 'difficulty', 'length', 'hiker']
