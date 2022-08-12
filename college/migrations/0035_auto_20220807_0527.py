# Generated by Django 3.2.12 on 2022-08-07 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0034_auto_20220807_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='Application_Status',
            field=models.TextField(blank=True, choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='Pending', editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='Bank',
            field=models.TextField(blank=True, choices=[('SBI', 'SBI'), ('PNB', 'PNB'), ('Axis', 'Axis')], default=' ', editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='Capital_Amount',
            field=models.IntegerField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='Interest',
            field=models.DecimalField(decimal_places=3, editable=False, max_digits=5, null=True),
        ),
    ]