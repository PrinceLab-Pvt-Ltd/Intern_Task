from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Student(models.Model):
    name = models.CharField(_("Name"), max_length=150)
    age = models.IntegerField(_("Age"))
    address = models.CharField(_("Address"), max_length=150)
    grade = models.CharField(_("Grade"), max_length=50)
    major = models.CharField(_("Major Subjects"), max_length=50)

    def __str__(self) -> str:
        return self.name
