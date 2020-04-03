from drf_yasg.utils import swagger_auto_schema
from profit_sharing.models import Department, Employee
from profit_sharing.serializers import (
    DepartmentSerializer,
    EmployeeProfitCaculatedSerializer,
    EmployeeSerializer,
    ProfitDistributionSerializer,
)
from profit_sharing.specifications import specifications
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


class DepartmentViewSet(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.people.all()
    serializer_class = EmployeeSerializer


class ProfitDistributionView(APIView):
    @staticmethod
    def build_serializer(employee):
        for spec, weights in specifications.items():
            if spec.is_satisfied_by(employee.as_dict()):
                return EmployeeProfitCaculatedSerializer(
                    instance=employee, calculation_weight=weights
                )
        return EmployeeProfitCaculatedSerializer(instance=employee)

    @swagger_auto_schema(request_body=ProfitDistributionSerializer())
    def post(self, request: Request, format=None):

        serializer = ProfitDistributionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        employees = Employee.people.select_related("department").all()

        employees_calculations = [
            self.build_serializer(instance).data for instance in employees
        ]

        distributed_sum = sum(
            [
                participation["valor_da_participação"]
                for participation in employees_calculations
            ]
        )

        available = serializer.validated_data["amount"] - distributed_sum

        result = {
            "participacoes": employees_calculations,
            "total_de_funcionarios": employees.count(),
            "total_distribuido": distributed_sum,
            "total_disponibilizado": serializer.validated_data["amount"],
            "saldo_total_disponibilizado": available,
        }
        return Response(result, content_type="application/json")
