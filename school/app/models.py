from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class ParentUser(User):
    parent_name = models.CharField(max_length=255)
    child_name = models.CharField(max_length=255)
    child_age = models.IntegerField
    lesson = models.Choices


class DZ(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=255)
    number = models.IntegerField
    file = models.FilePathField
