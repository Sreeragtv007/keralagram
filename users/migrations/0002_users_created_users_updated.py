# Generated by Django 4.2 on 2025-01-02 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='users',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
