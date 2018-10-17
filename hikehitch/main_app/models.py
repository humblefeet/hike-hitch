from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from django import forms

DIFFICULTY = (
    ('1', 'Easy'),
    ('2', 'Moderate'),
    ('3', 'Hard'),
    ('4', 'Advanced'),
    ('5', 'Extreme')
)
EXPERIENCE = (
    ('1', 'Beginner'),
    ('2', 'Intermediate'),
    ('3', 'Experienced'),
    ('4', 'Advanced')
)

SEX  = (
    ('f', 'Female'),
    ('m', 'Male'),
    ('o', 'other')
)
# Create your models here.

class Trail(models.Model):
    name = models.CharField(max_length=100)
    length = models.IntegerField()
    difficulty = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=DIFFICULTY,
        # set the default value for meal to be 'B'
        default=DIFFICULTY[0][0])
    location = models.CharField(max_length=200)
        
    def __str__(self):
        return self.name



class Hiker(models.Model):
    first_name = models.CharField(max_length=50)
    age = models.IntegerField()
    sex = models.CharField(
        max_length=1,
        choices=SEX
    )
    experience = models.CharField(
        max_length=1,
        choices = EXPERIENCE,
        default = EXPERIENCE[0][0]
    )
    email = models.EmailField()
    social_media = models.URLField()
    bio = models.TextField(max_length=400)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.first_name
    def get_absolute_url(self):
        return reverse('profile', kwargs={'hiker_id': self.id})


class Trip(models.Model):
    date = models.DateField()
    user = models.ManyToManyField(User)
    length = models.IntegerField(
        default=0
    )
    difficulty= models.CharField(
        max_length=1,
        choices=DIFFICULTY,
        default=DIFFICULTY[0][0]
    )
    trail = models.ManyToManyField(Trail)