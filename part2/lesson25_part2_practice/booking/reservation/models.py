from uuid import uuid4

from django.db import models


class VISAS:
    DEFAULT = 0
    ONLINE = 1
    SCHENGEN = 2

    ALL = {DEFAULT: 'Нужна виза',
           ONLINE: 'Виза не нужна',
           SCHENGEN: 'У меня есть шенген'}


class COVID_STATUSES:
    DEFAULT = 0
    BAN_OR_RESTRICTION_COUNTRIES = 1
    BAN = 2

    ALL = {
        DEFAULT: 'Нет ограничений',
        BAN_OR_RESTRICTION_COUNTRIES: 'Закрыт или ограничен въезд для пассажиров, побывавших в определенных странах',
        BAN: 'Въезд запрещен'
    }


class Feedback(models.Model):
    STATUS = [(1, "published"), (2, "not published")]

    correlation_id = models.UUIDField(default=uuid4, editable=False, unique=True)
    user_feedback = models.IntegerField(null=True, choices=STATUS)
    user_feedback_timestamp = models.DateTimeField(null=True)
    user_photo = models.TextField(blank=True, null=True, max_length=256)
    user_photo_timestamp = models.DateTimeField(null=True)
    closed = models.BooleanField(default=False)


class Destination(models.Model):
    class Meta:
        db_table = 'summaries_destinations'
        verbose_name = 'destination'
        verbose_name_plural = 'destinations'

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='')
    to_name = models.CharField(max_length=100, null=True, blank=True)
    flag = models.CharField(max_length=10, null=True, blank=True)
    visa_id = models.PositiveSmallIntegerField(choices=VISAS.ALL.items(), null=True, blank=True)
    covid_status = models.PositiveSmallIntegerField(choices=COVID_STATUSES.ALL.items(), default=COVID_STATUSES.DEFAULT)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    title = models.CharField('Заголовок', max_length=300)
    icon = models.ImageField('Иконка', upload_to='reservations/icons')
    logo = models.ImageField('Логотип', upload_to='reservations/logos')
    link = models.CharField('Ссылка', max_length=300)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
        db_table = 'reserverions_reservations'
