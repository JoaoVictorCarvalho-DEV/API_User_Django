from django.db import models

class User(models.Model):
    user_cpf = models.CharField(max_length=11, primary_key=True, default='')
    user_name = models.CharField(max_length=150, default='')
    user_age = models.IntegerField(default=0)
    user_telephone = models.IntegerField(default=0)
    user_email = models.EmailField(default='')

    def __str__(self):
        return f'Nome: {self.user_name} || Email: {self.user_email}'