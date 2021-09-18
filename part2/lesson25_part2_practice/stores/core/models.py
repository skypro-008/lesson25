from django.db import models


class Store(models.Model):
    STATUS = [
        ("new", "Новый"),
    ]

    slug = models.CharField(max_length=10)
    # TODO
