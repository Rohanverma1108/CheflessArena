# Generated by Django 2.1.4 on 2018-12-07 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('migApp', '0006_auto_20181207_0603'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='migApp.Restaurant'),
        ),
    ]
