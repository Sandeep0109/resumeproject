from django.db import models 

# Create your models here.
class Contact(models.Model):
    userId=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=50,default='')
    subject=models.CharField(max_length=50,default='')
    massage=models.CharField(max_length=250,default='')