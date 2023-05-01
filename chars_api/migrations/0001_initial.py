# Generated by Django 4.2 on 2023-04-29 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('type', models.CharField(max_length=16)),
                ('level', models.IntegerField()),
                ('str', models.IntegerField()),
                ('dex', models.IntegerField()),
                ('con', models.IntegerField()),
                ('int', models.IntegerField()),
                ('wis', models.IntegerField()),
                ('cha', models.IntegerField()),
            ],
        ),
    ]
