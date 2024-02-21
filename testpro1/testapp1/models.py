from django.db import models

class Student(models.Model):
    
    roll_no = models.IntegerField()
    name = models.CharField(max_length = 45)
    marks = models.IntegerField()
    address = models.TextField()
