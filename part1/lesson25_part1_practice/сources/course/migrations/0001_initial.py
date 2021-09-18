# Generated by Django 3.2.6 on 2021-09-13 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=1000)),
                ('start_day', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('new', 'Новый'), ('started', 'В процессе'), ('closed', 'Закончился')], default='new', max_length=7)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
