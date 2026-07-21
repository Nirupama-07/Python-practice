from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.name