from django.db import models
from django.utils.translation import gettext_lazy as _


class Member(models.Model):
    class Role(models.TextChoices):
        ADMIN = "ADM", _("Administrator")
        REGULAR = "REG", _("Regular")

    role = models.CharField(max_length=3, choices=Role.choices, default=Role.REGULAR)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=256, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
