from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)


