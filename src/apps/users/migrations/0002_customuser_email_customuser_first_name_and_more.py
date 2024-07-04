# Generated by Django 4.2 on 2024-07-03 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]