# Generated by Django 3.1.4 on 2020-12-14 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='codigo',
            field=models.CharField(default=111, max_length=16),
            preserve_default=False,
        ),
    ]
