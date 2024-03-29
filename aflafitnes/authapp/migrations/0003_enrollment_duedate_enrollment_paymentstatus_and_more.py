# Generated by Django 4.2.7 on 2024-02-16 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_enrollment_membershipplan_trainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='DueDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='paymentStatus',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='price',
            field=models.IntegerField(blank=True, max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='membershipplan',
            name='price',
            field=models.IntegerField(max_length=55),
        ),
    ]
