# Generated by Django 2.2.5 on 2019-09-20 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoggedUser',
            fields=[
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
    ]