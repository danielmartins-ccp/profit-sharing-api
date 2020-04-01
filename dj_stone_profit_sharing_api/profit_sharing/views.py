from profit_sharing.models import Department, Employee
from profit_sharing.serializers import DepartmentSerializer, EmployeeSerializer
from rest_framework.viewsets import ModelViewSet


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.people.all()
    serializer_class = EmployeeSerializer
