from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import StudentsForm
from .models import Student

# Create your views here.


class StudentCreateView(CreateView):
    form_class = StudentsForm
    model = Student
    success_url = reverse_lazy("students-entry:list")


class StudentListView(ListView):
    model = Student
    form = StudentsForm


class StudentUpdateView(UpdateView):
    form_class = StudentsForm
    model = Student
    success_url = reverse_lazy("students-entry:list")


update = StudentUpdateView.as_view()


class StudentDeleteview(DeleteView):
    model = Student
    form_class = StudentsForm
    success_url = reverse_lazy("students-entry:list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


def delete_student(request, pk):
    Student.objects.get(pk=pk).delete()
    return redirect("students-entry:list")


delete = delete_student
# delete = StudentDeleteview.as_view()
