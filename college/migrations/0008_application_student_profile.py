# Generated by Django 3.1.7 on 2021-07-14 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0007_delete_application_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='student_profile',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
