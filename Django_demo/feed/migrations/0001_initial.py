# Generated by Django 3.2.5 on 2021-08-02 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=20)),
                ('token', models.CharField(max_length=30)),
            ],
        ),
    ]
