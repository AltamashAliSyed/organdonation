# Generated by Django 4.2.6 on 2025-02-11 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_remove_donor_user_remove_hospital_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='address',
            field=models.CharField(default=11, max_length=500),
            preserve_default=False,
        ),
    ]
