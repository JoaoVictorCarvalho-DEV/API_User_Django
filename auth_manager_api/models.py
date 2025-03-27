from django.db import models

# Create your models here.
class Atores(models.Model):
    class Meta:
        db_table = "atores"

    nome = models.CharField(max_length=255)
    email = models.EmailField()
    papel = models.CharField(max_length=50)
