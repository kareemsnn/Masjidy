# Generated by Django 5.0.6 on 2024-06-17 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_rename_lat_customuser_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mosque',
            name='nonprofitform',
            field=models.FileField(default='placeholder.pdf', upload_to='mosque_verification/'),
        ),
    ]
