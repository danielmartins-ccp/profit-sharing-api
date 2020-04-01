from django.db import models
from profit_sharing.managers import EmployeeQuerySet


class Timestampable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Department(Timestampable, models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"


class Employee(Timestampable, models.Model):
    registration_number = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    raw_salary = models.DecimalField(max_digits=10, decimal_places=2)
    admission_date = models.DateField()
    people = EmployeeQuerySet.as_manager()

    def __str__(self):
        return f"[{self.registration_number}] {self.name}"
