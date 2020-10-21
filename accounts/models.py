from django.db import models
from django.contrib.auth.models import AbstractUser

class Member(AbstractUser):
    username = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    contribution = models.CharField(max_length=200, blank=True, null=True)
    percentage = models.DecimalField(max_digits=19,decimal_places=2, default=1)
    account_no = models.CharField(max_length=200, blank=True, null=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    