# Generated by Django 5.0.3 on 2024-03-18 13:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_customuser_donated_alter_customuser_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate_food',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food_donations_received', to='api.customuser'),
        ),
        migrations.AlterField(
            model_name='donate_food',
            name='status',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='donate_grocery',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grocery_donations_received', to='api.customuser'),
        ),
        migrations.AlterField(
            model_name='donate_grocery',
            name='status',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='helper',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests_helped', to='api.customuser'),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
