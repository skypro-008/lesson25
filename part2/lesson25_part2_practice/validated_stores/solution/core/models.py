from django.core.exceptions import ValidationError
from django.db import models


def check_google(value):
   if value and not value.endswith("google.com"):
       raise ValidationError(
           '%(value)s not in google.com',
           params={'value': value},
       )


class Store(models.Model):
    STATUS = [
        ("new", "Новый"),
        ("open", "Открыт"),
        ("closed", "Закрыт"),
    ]

    slug = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=120)
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=6, default="new", choices=STATUS)
    contact_email = models.EmailField(null=True, blank=True, validators=[check_google])
    opens_at = models.TimeField(null=True, blank=True)
    closes_at = models.TimeField(null=True, blank=True)
    is_cash_only = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)