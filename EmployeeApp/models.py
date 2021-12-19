from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)


class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    Department = models.ForeignKey(Departments, on_delete=DO_NOTHING)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=100)