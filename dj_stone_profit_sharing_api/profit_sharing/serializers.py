import decimal

from profit_sharing.models import Department, Employee
from rest_framework import fields
from rest_framework.serializers import ModelSerializer, Serializer


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class EmployeeProfitSerializer(ModelSerializer):
    matricula = fields.CharField(source="registration_number")
    nome = fields.CharField(source="name")
    valor_da_participação = fields.DecimalField(
        source="profit_calculation",
        max_digits=10,
        decimal_places=2,
        rounding=decimal.ROUND_UP,
        coerce_to_string=True,
    )

    class Meta:
        model = Employee
        fields = ["matricula", "nome", "valor_da_participação"]


class DistributionPayloadSerializer(Serializer):
    valor_para_distribuicao = fields.DecimalField(
        max_digits=10, decimal_places=2, source="amount"
    )


class DistributedProfitResponseSerializer(Serializer):
    participacoes = EmployeeProfitSerializer(many=True)
    total_de_funcionarios = fields.IntegerField()
    total_distribuido = fields.DecimalField(
        max_digits=10,
        decimal_places=2,
        rounding=decimal.ROUND_UP,
        coerce_to_string=True,
        required=False,
    )
    total_disponibilizado = fields.DecimalField(
        max_digits=10, decimal_places=2, rounding=decimal.ROUND_UP,
    )
    saldo_total_disponibilizado = fields.DecimalField(
        max_digits=10, decimal_places=2, rounding=decimal.ROUND_UP, required=False
    )

    def validate(self, attrs):
        distributed_sum = sum(
            [
                participation["profit_calculation"]
                for participation in attrs["participacoes"]
            ]
        )
        available = attrs["total_disponibilizado"] - distributed_sum
        attrs["saldo_total_disponibilizado"] = available
        attrs["total_distribuido"] = distributed_sum
        return attrs
