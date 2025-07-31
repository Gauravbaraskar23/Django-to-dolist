from django.db import models

class test(models.Model):
    startdete = models.CharField(max_length=200)
    enddete = models.CharField(max_length=200)
    taskname = models.CharField(max_length=200)
    
    
# Create your models here.
