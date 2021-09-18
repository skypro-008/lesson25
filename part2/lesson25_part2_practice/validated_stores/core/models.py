from django.db import models


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
    contact_email = models.EmailField(null=True, blank=True)  # TODO: провалидируй меня
    opens_at = models.TimeField(null=True, blank=True)
    closes_at = models.TimeField(null=True, blank=True)
    is_cash_only = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
