# Generated by Django 5.0.1 on 2024-02-06 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0011_profileuser_req'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profileuser',
            name='req',
        ),
        migrations.AddField(
            model_name='profileuser',
            name='requestRole',
            field=models.CharField(default='U', max_length=10),
        ),
    ]