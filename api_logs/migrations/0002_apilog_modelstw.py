# Generated by Django 4.2.13 on 2024-12-17 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_logs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apilog',
            name='modelstw',
            field=models.TextField(default='linear model'),
            preserve_default=False,
        ),
    ]
