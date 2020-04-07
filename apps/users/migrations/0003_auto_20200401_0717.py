# Generated by Django 3.0.3 on 2020-04-01 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200327_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPrivate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_private', models.BooleanField(default=False, help_text='Designates if other users can view email address in profile', verbose_name='email private')),
                ('first_name_private', models.BooleanField(default=False, help_text='Designates if other users can view first name in profile', verbose_name='first name private')),
                ('last_name_private', models.BooleanField(default=False, help_text='Designates if other users can view last name in profile', verbose_name='last name private')),
                ('dob_private', models.BooleanField(default=False, help_text='Designates if other users can view dob in profile', verbose_name='dob private')),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='dob',
        ),
        migrations.AddField(
            model_name='user',
            name='dob',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='dob'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=40, null=True, verbose_name='first name'),
        ),
    ]