from django.db import models
from django.db import models

class employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    address=models.TextField()
    phone=models.CharField(max_length=100)  
# Create your models here.
