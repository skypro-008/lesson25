# Generated by Django 3.2.7 on 2021-09-10 10:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='slug',
            field=models.SlugField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vacancy',
            name='status',
            field=models.CharField(choices=[('draft', 'Черновик'), ('open', 'Открыта'), ('closed', 'Closed')], default='draft', max_length=10),
        ),
    ]
