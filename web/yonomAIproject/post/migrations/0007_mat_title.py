# Generated by Django 3.1.1 on 2020-09-20 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_mat'),
    ]

    operations = [
        migrations.AddField(
            model_name='mat',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
