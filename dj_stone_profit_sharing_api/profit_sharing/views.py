from drf_yasg.utils import swagger_auto_schema
from profit_sharing.models import Department, Employee
from profit_sharing.serializers import (
    DepartmentSerializer,
    DistributedProfitResponseSerializer,
    DistributionPayloadSerializer,
    EmployeeSerializer,
)
from rest_framework.permissions import AllowAny
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
    authentication_classes = ()
    permission_classes = [AllowAny]

    @swagger_auto_schema(request_body=DistributionPayloadSerializer())
    def post(self, request: Request, format=None):

        serializer = DistributionPayloadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employees = Employee.people.select_related("department").all()

        weights = [people.get_weight() for people in employees]

        result = DistributedProfitResponseSerializer(
            data={
                "participacoes": [
                    {
                        "matricula": instance.registration_number,
                        "nome": instance.name,
                        "valor_da_participação": instance.proportional_profit_calculation(
                            serializer.validated_data["amount"], weights,
                        ),
                    }
                    for instance in employees
                ],
                "total_de_funcionarios": employees.count(),
                "total_disponibilizado": serializer.validated_data["amount"],
            }
        )
        result.is_valid(raise_exception=True)
        return Response(result.data, content_type="application/json",)
