from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    course = models.CharField(max_length=50)

    def __str__(self):
        return self.name
