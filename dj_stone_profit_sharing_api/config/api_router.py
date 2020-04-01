from django.conf import settings
from profit_sharing.views import DepartmentViewSet, EmployeeViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

from dj_stone_profit_sharing_api.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("departments", DepartmentViewSet)
router.register("employees", EmployeeViewSet)


app_name = "api"
urlpatterns = router.urls
