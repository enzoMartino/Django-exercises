# Generated by Django 2.0.2 on 2018-04-24 00:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_auto_20180424_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]