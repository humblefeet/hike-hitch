from django.db import models
from django.contrib.auth.models import User

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
        
    def __str__(self):
        return self.name

class Hiker(models.Model):
    first_name = models.CharField(max_length=50)
    age = models.IntegerField()
    sex = models.CharField(
        max_length=1,
        choices=SEX,)
    experience = models.CharField(
        max_length=1,
        choices = EXPERIENCE,
        default = EXPERIENCE[0][0]
    )
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name