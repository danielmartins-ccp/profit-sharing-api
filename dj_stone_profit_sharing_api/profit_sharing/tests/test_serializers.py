import io

import pytest
from assertpy import assert_that
from jsonschema import validate
from model_bakery import baker
from profit_sharing.models import Department, Employee
from profit_sharing.serializers import DepartmentSerializer, EmployeeSerializer
from rest_framework.parsers import JSONParser


@pytest.mark.django_db
def test_department_serialization(schema_loader):
    # GIVEN
    department = baker.make(Department)

    # WHEN
    serializer = DepartmentSerializer(department)

    # THEN
    validate(
        serializer.data, schema=schema_loader("department"),
    )


@pytest.mark.django_db
def test_department_deserialization(schema_loader):
    # GIVEN
    stream = io.BytesIO(
        b"""
        {
            "id": 1,
            "created_at": "2020-04-01T03:44:26.542343Z",
            "modified_at": "2020-04-01T03:44:26.542376Z",
            "name": "Diretoria"
        }
    """
    )

    # WHEN
    data = JSONParser().parse(stream)
    serializer = DepartmentSerializer(data=data)
    serializer.is_valid()

    # THEN
    assert_that(serializer.validated_data).contains_key("name")


@pytest.mark.django_db
def test_employee_serialization(schema_loader):
    # GIVEN
    employee = baker.make(Employee)

    # WHEN
    serializer = EmployeeSerializer(employee)

    # THEN
    validate(
        serializer.data, schema=schema_loader("employee"),
    )


@pytest.mark.django_db
def test_employee_deserialization(schema_loader):

    # GIVEN
    baker.make(Department, id=1)
    stream = io.BytesIO(
        b"""
        {
            "id": 1,
            "created_at": "2020-04-01T03:45:08.076041Z",
            "modified_at": "2020-04-01T03:45:08.076076Z",
            "registration_number": "0009968",
            "name": "Victor Wilson",
            "position": "Diretor Financeiro",
            "raw_salary": "12696.20",
            "admission_date": "2012-01-05",
            "department": 1
        }
    """
    )

    # WHEN
    data = JSONParser().parse(stream)
    serializer = EmployeeSerializer(data=data)
    serializer.is_valid()

    # THEN
    assert_that(serializer.validated_data).contains_key(
        "name",
        "raw_salary",
        "department",
        "admission_date",
        "registration_number",
        "position",
    )
