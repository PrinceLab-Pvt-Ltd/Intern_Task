from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StudentListView, StudentCreateView, update, delete
from .api_views import StudentModelView

r = DefaultRouter()
r.register(r"student", StudentModelView, basename="student")
app_name = "students-entry"
urlpatterns = [
    # students-entry:list
    path("", StudentListView.as_view(), name="list"),
    path("create", StudentCreateView.as_view(), name="create"),
    path("update/<int:pk>", update, name="update"),
    path("delete/<int:pk>", delete, name="delete"),
    path("api/student/list", StudentModelView.as_view(actions={"get": "list"})),
]
if settings.DEBUG:
    urlpatterns += [path("api/", include(r.urls))]
