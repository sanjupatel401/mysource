# Generated by Django 4.1.7 on 2023-08-10 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_upload_project_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_project',
            name='upload_date',
            field=models.DateField(auto_created=True, auto_now_add=True),
        ),
    ]
