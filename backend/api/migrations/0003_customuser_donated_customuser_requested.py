# Generated by Django 5.0.3 on 2024-03-18 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_donate_food_donate_grocery_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='donated',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='requested',
            field=models.IntegerField(default=0),
        ),
    ]