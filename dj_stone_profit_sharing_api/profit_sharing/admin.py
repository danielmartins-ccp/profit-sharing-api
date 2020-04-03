from django.contrib import admin
from profit_sharing.filters import AdmissionDateListFilter
from profit_sharing.models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["name", "raw_salary", "department", "admission_date"]
    list_filter = [
        "name",
        "raw_salary",
        "department",
        "admission_date",
        AdmissionDateListFilter,
    ]
