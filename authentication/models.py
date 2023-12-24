from enum import Enum

from django.contrib.auth.models import AbstractUser
from django.db import models

from authentication.managers import UserManager


class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'


class CustomUser(AbstractUser):

    id = models.AutoField(primary_key=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(
        max_length=10, choices=[(gender.name, gender.value) for gender in Gender], blank=True, null=True
    )
    is_paid = models.BooleanField(null=False, default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}' if self.first_name and self.last_name else self.username

    objects = UserManager()