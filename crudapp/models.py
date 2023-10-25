from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100,verbose_name="Student Name")
    email = models.CharField(max_length=250,verbose_name="Student Email")

    def __str__(self):
        return str(self.id)