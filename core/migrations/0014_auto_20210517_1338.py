# Generated by Django 3.1.7 on 2021-05-17 07:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0013_auto_20210331_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='readers',
            field=models.ManyToManyField(blank=True, related_name='readed_articles', to=settings.AUTH_USER_MODEL, verbose_name='Читатели'),
        ),
    ]
