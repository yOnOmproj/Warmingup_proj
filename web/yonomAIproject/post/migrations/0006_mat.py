# Generated by Django 3.1.1 on 2020-09-20 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20200917_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='mat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mat', models.FileField(null=True, upload_to='mat')),
            ],
        ),
    ]
