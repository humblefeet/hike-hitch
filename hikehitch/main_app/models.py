from django.db import models
from django.contrib.auth.models import User

DIFFICULTY = (
    ('1', 'Easy'),
    ('2', 'Moderate'),
    ('3', 'Hard'),
    ('4', 'Advanced'),
    ('5', 'Extreme')
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