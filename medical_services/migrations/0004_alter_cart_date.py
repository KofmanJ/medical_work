# Generated by Django 5.0.4 on 2024-05-04 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_services', '0003_cart_delete_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата и время'),
        ),
    ]
