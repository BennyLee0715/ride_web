from django.db import models

# Create your models here.
class User(models.Model):
    '''user list'''
    name = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    def __str__(self):
        return self.name