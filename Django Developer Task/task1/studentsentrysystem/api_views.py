from .models import Student
from .serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet


class StudentModelView(ModelViewSet):
    # model = Student
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
