from django.db import models

class User(models.Model):
    cpf = models.CharField(max_length=11, default='')
    name = models.CharField(max_length=150, default='')
    age = models.IntegerField(default=0)
    telephone = models.IntegerField(default=0)
    email = models.EmailField(default='')
    password = models.CharField(max_length=50, default='')
