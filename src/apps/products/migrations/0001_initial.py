# Generated by Django 4.2 on 2024-07-04 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ingredients', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('photo', models.ImageField(upload_to='product_photos/')),
                ('popularity', models.IntegerField(default=0)),
                ('novelty', models.DateTimeField(auto_now_add=True)),
                ('type', models.CharField(choices=[('salad', 'Salad')], max_length=50)),
            ],
        ),
    ]
