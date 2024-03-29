# Generated by Django 3.1.7 on 2021-03-31 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20210331_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleimage',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='core.article'),
            preserve_default=False,
        ),
    ]
