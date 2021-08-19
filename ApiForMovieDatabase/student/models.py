from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.IntegerField()
    dept = models.CharField(max_length=100)
    session = models.CharField(max_length=100)
    institute = models.CharField(max_length=100)
    
    def __str__(self):
       return self.name 