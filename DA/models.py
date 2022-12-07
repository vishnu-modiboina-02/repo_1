from django.db import models

# Create your models here.

class charger(models.Model):
    name=models.CharField(max_length=40)
    roll_no=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=100,default='abcfdshgfggfd')
