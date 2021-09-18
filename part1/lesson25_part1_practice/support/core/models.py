from datetime import datetime

from django.db import models


class Statistic(models.Model):
    UNANSWERED_BUTTONS = [
        ("unk", "Не известно"),
        ("R_t", "Не хватило времени"),
        ("R_f", "Форс-мажор"),
        ("R_i", "Техническая проблема"),
    ]

    store = models.CharField(max_length=100)
    author = models.CharField(max_length=120)
    status = models.CharField(max_length=100, blank=True, db_index=True)
    day = models.DateField(null=False)
    reason = models.CharField(max_length=3, default="unk", choices=UNANSWERED_BUTTONS)
    timestamp = models.DateTimeField(default=datetime.now)


class Issue(models.Model):
    uid = models.CharField(verbose_name="Номер обращения", max_length=15, null=False)
    author = models.CharField(max_length=120)
    timestamp = models.DateTimeField(verbose_name="Время создания", auto_now=True)
    text = models.TextField(verbose_name="Описание проблемы", blank=True, default="")
    photos = models.URLField(max_length=200, blank=True)