from django.db import models

# Create your models here.
class Accounts(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

class Login(models.Model):
    username = ""
    password = ""

class SignUp(models.Model):
    username = ""
    password = ""

class LogOut(models.Model):
    username = ""
    password = ""