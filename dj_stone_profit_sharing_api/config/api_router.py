from django.conf import settings
from django.urls import path
from profit_sharing.views import (
    DepartmentViewSet,
    EmployeeViewSet,
    ProfitDistributionView,
)
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

# router.register("users", UserViewSet)
router.register("departments", DepartmentViewSet)
router.register("employees", EmployeeViewSet)


app_name = "api"
urlpatterns = router.urls + [
    path("calculate/", view=ProfitDistributionView.as_view(), name="calculate"),
]
