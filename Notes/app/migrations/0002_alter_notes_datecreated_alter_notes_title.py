# Generated by Django 5.0.dev20230505072651 on 2023-06-17 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
