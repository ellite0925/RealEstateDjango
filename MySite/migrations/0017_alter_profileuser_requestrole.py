# Generated by Django 5.0.1 on 2024-02-15 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MySite', '0016_remove_property_house_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='requestRole',
            field=models.CharField(default='Normal User', max_length=10),
        ),
    ]