# Generated by Django 3.0.3 on 2020-04-16 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20200416_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='display_name',
            field=models.CharField(blank=True, max_length=14, null=True, unique=True, verbose_name='username'),
        ),
    ]
