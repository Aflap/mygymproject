# Generated by Django 4.2.7 on 2024-02-20 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_rename_galle_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Selectdate', models.DateTimeField(auto_now_add=True)),
                ('Login', models.CharField(max_length=200)),
                ('Logout', models.CharField(max_length=200)),
                ('SelectWorkout', models.CharField(max_length=100)),
                ('TrainedBy', models.CharField(max_length=100)),
            ],
        ),
    ]