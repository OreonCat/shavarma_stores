from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    photo = models.ImageField(upload_to="users/", null=True, blank=True, verbose_name="Аватарка")
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Дата рождения")
