# Generated by Django 3.2.9 on 2021-11-18 15:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='createdon',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
